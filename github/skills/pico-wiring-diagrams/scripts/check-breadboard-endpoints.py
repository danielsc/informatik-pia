#!/usr/bin/env python3

import argparse
import math
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


WIRE_CONTACT_COLORS = {
    "wire-red": "#dc2626",
    "wire-black": "#111827",
    "wire-yellow": "#ca8a04",
    "wire-input": "#2563eb",
    "wire-output": "#16a34a",
    "wire-violet": "#7c3aed",
}


class EndpointParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.breadboard = None
        self.fields = []
        self.connections_layer = False
        self._connections_depth = 0
        self.electrical_elements = []
        self.contact_markers = []
        self.obstructions = []
        self.component_dimensions = {}
        self.component_uses = []
        self._defs_depth = 0
        self.structure_errors = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        element_id = attributes.get("id")
        if tag == "defs":
            self._defs_depth += 1
        if tag == "rect" and element_id == "breadboard":
            self.breadboard = attributes
        if tag == "rect" and attributes.get("data-breadboard-hole-field") == "true":
            self.fields.append(attributes)
        if "data-obscures-holes" in attributes:
            self.obstructions.append(attributes["data-obscures-holes"])
        if (
            tag == "symbol"
            and attributes.get("id", "").startswith("component-")
        ):
            self.component_dimensions[attributes["id"]] = attributes.get(
                "viewbox", ""
            )
        if (
            tag == "use"
            and attributes.get("href", "").startswith("#component-")
            and self._defs_depth == 0
        ):
            self.component_uses.append(attributes)
            if "data-obscures-holes" not in attributes:
                self.structure_errors.append(
                    "Every placed component must declare data-obscures-holes"
                )
        if tag == "g" and element_id == "circuit-connections":
            self.connections_layer = True
            self._connections_depth = 1
            return

        in_connections = self._connections_depth > 0
        if in_connections and "transform" in attributes:
            self.structure_errors.append(
                "Transforms are not allowed inside #circuit-connections"
            )
        if "data-connection-kind" in attributes and not in_connections:
            self.structure_errors.append(
                "Electrical element is outside #circuit-connections"
            )
        if "data-contact-marker" in attributes and not in_connections:
            self.structure_errors.append(
                "Contact marker is outside #circuit-connections"
            )
        if in_connections and "data-connection-kind" in attributes:
            self.electrical_elements.append((tag, attributes))
        if (
            in_connections
            and tag == "circle"
            and attributes.get("data-contact-marker") == "true"
        ):
            if "data-connection-kind" in attributes:
                self.structure_errors.append(
                    "Visual contact markers must not declare a physical contact"
                )
            self.contact_markers.append(attributes)
        if in_connections and tag == "g":
            self._connections_depth += 1

    def handle_endtag(self, tag):
        if tag == "g" and self._connections_depth > 0:
            self._connections_depth -= 1
        if tag == "defs" and self._defs_depth > 0:
            self._defs_depth -= 1


def number(attributes, name):
    try:
        return float(attributes[name])
    except (KeyError, ValueError) as error:
        raise ValueError(f"Missing or invalid {name}") from error


def parse_points(value):
    values = [
        float(item)
        for item in re.split(r"[\s,]+", value.strip())
        if item
    ]
    if len(values) < 4 or len(values) % 2:
        raise ValueError("Polyline points must contain at least two X,Y pairs")
    return list(zip(values[0::2], values[1::2]))


def parse_obstructions(values):
    rectangles = []
    for value in values:
        for item in value.split(";"):
            coordinates = [
                float(number)
                for number in re.split(r"[\s,]+", item.strip())
                if number
            ]
            if len(coordinates) != 4:
                raise ValueError(
                    "data-obscures-holes requires x1,y1,x2,y2 rectangles"
                )
            x1, y1, x2, y2 = coordinates
            if x1 > x2 or y1 > y2:
                raise ValueError(
                    "data-obscures-holes rectangle bounds are reversed"
                )
            rectangles.append((x1, y1, x2, y2))
    return rectangles


def component_size_errors(document):
    errors = []
    for attributes in document.component_uses:
        component_id = attributes["href"][1:]
        viewbox = document.component_dimensions.get(component_id, "")
        values = [
            float(number)
            for number in re.split(r"[\s,]+", viewbox.strip())
            if number
        ]
        if len(values) != 4:
            errors.append(f"{component_id} has no valid local viewBox")
            continue
        expected_width, expected_height = values[2], values[3]
        try:
            actual_width = float(attributes["width"])
            actual_height = float(attributes["height"])
        except (KeyError, ValueError):
            errors.append(f"{component_id} use has no valid width and height")
            continue
        if not (
            math.isclose(actual_width, expected_width, abs_tol=1e-9)
            and math.isclose(actual_height, expected_height, abs_tol=1e-9)
        ):
            errors.append(
                f"{component_id} must use canonical "
                f"{expected_width:g}x{expected_height:g} dimensions"
            )
    return errors


def rendered_endpoints(tag, attributes):
    ends = attributes.get("data-breadboard-ends")
    if tag == "line":
        points = [
            (number(attributes, "x1"), number(attributes, "y1")),
            (number(attributes, "x2"), number(attributes, "y2")),
        ]
    elif tag == "polyline":
        points = parse_points(attributes.get("points", ""))
    elif tag == "circle" and ends == "center":
        return [(number(attributes, "cx"), number(attributes, "cy"))]
    else:
        raise ValueError(
            f"<{tag}> is unsupported for data-breadboard-ends={ends!r}"
        )

    if ends == "start":
        return [points[0]]
    if ends == "end":
        return [points[-1]]
    if ends == "both":
        return [points[0], points[-1]]
    raise ValueError(f"Invalid data-breadboard-ends={ends!r}")


def contact_requirements(tag, attributes):
    kind = attributes.get("data-connection-kind")
    ends = attributes.get("data-breadboard-ends")
    points = rendered_endpoints(tag, attributes)
    if tag == "circle":
        color = attributes.get("data-contact-color")
        if not color:
            raise ValueError("Connector circle is missing data-contact-color")
        return [(points[0], color, True)]

    roles = {
        "start": ["start"],
        "end": ["end"],
        "both": ["start", "end"],
    }.get(ends)
    if roles is None:
        raise ValueError(f"Invalid electrical endpoint declaration {ends!r}")
    classes = attributes.get("class", "").split()
    default_color = next(
        (WIRE_CONTACT_COLORS[name] for name in classes if name in WIRE_CONTACT_COLORS),
        attributes.get("data-contact-color"),
    )
    requirements = []
    for point, role in zip(points, roles):
        color = attributes.get(
            f"data-contact-{role}-color",
            default_color,
        )
        if not color:
            raise ValueError(
                f"{kind} {role} endpoint is missing its contact colour"
            )
        requirements.append((point, color, False))
    return requirements


def grid_index(value, origin, pitch):
    return round((value - origin) / pitch)


def hole_at(point, fields, origin_x, origin_y, pitch_x, pitch_y):
    x, y = point
    column = grid_index(x, origin_x, pitch_x)
    row = grid_index(y, origin_y, pitch_y)
    hole_x = origin_x + column * pitch_x
    hole_y = origin_y + row * pitch_y
    in_field = any(
        number(field, "x") <= hole_x < number(field, "x") + number(field, "width")
        and number(field, "y") <= hole_y < number(field, "y") + number(field, "height")
        for field in fields
    )
    return hole_x, hole_y, in_field


def score_error(error):
    if math.isclose(error, 0.0, abs_tol=1e-9):
        return 4
    if error <= 0.5:
        return 3
    if error <= 1:
        return 2
    if error <= 2:
        return 1
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Check electrical contacts against visible breadboard holes."
    )
    parser.add_argument("diagram", type=Path)
    args = parser.parse_args()

    source = args.diagram.read_text(encoding="utf-8")
    document = EndpointParser()
    document.feed(source)
    document.structure_errors.extend(component_size_errors(document))

    if document.breadboard is None or len(document.fields) != 4:
        print("Expected breadboard geometry and four visible hole fields.", file=sys.stderr)
        return 1
    if not document.connections_layer:
        print("Missing #circuit-connections layer.", file=sys.stderr)
        return 1
    if document.structure_errors:
        print(document.structure_errors[0], file=sys.stderr)
        return 1

    try:
        origin_x = number(document.breadboard, "data-hole-origin-x")
        origin_y = number(document.breadboard, "data-hole-origin-y")
        pitch_x = number(document.breadboard, "data-hole-pitch-x")
        pitch_y = number(document.breadboard, "data-hole-pitch-y")
        obstructions = parse_obstructions(document.obstructions)
        endpoints = []
        contact_requirements_by_element = []
        for element_index, (tag, attributes) in enumerate(
            document.electrical_elements, start=1
        ):
            if attributes["data-connection-kind"] not in {
                "wire",
                "component",
                "connector",
            }:
                raise ValueError(
                    "Invalid data-connection-kind="
                    f"{attributes['data-connection-kind']!r}"
                )
            endpoints.extend(
                (point, element_index, tag)
                for point in rendered_endpoints(tag, attributes)
            )
            contact_requirements_by_element.extend(
                (point, color.lower(), is_circle, element_index)
                for point, color, is_circle in contact_requirements(
                    tag, attributes
                )
            )
        contact_markers = [
            (
                (number(marker, "cx"), number(marker, "cy")),
                marker.get("fill", "").lower(),
            )
            for marker in document.contact_markers
        ]
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    errors = []
    outside = []
    obscured = []
    marker_errors = []
    occupied_holes = {}
    for point, element_index, tag in endpoints:
        hole_x, hole_y, in_field = hole_at(
            point, document.fields, origin_x, origin_y, pitch_x, pitch_y
        )
        errors.extend((abs(point[0] - hole_x), abs(point[1] - hole_y)))
        if not in_field:
            outside.append(point)
        if any(
            x1 <= hole_x <= x2 and y1 <= hole_y <= y2
            for x1, y1, x2, y2 in obstructions
        ):
            obscured.append((point, element_index, tag))
        hole = (
            grid_index(hole_x, origin_x, pitch_x),
            grid_index(hole_y, origin_y, pitch_y),
        )
        occupied_holes.setdefault(hole, []).append(
            (element_index, tag, point)
        )

    marker_set = set(contact_markers)
    for point, color, is_circle, element_index in contact_requirements_by_element:
        if is_circle:
            _, attributes = document.electrical_elements[element_index - 1]
            if attributes.get("fill", "").lower() != color:
                marker_errors.append(
                    (point, element_index, "connector circle colour differs")
                )
        elif (point, color) not in marker_set:
            marker_errors.append(
                (point, element_index, f"missing {color} contact marker")
            )

    maximum_error = max(errors, default=0.0)
    shared_holes = {
        hole: contacts
        for hole, contacts in occupied_holes.items()
        if len(contacts) > 1
    }
    score = (
        0
        if outside or shared_holes or obscured or marker_errors
        else score_error(maximum_error)
    )
    print(f"Electrical elements: {len(document.electrical_elements)}")
    print(f"Endpoints checked:   {len(endpoints)}")
    print(f"Maximum axis error:  {maximum_error:.2f}px")
    print(f"Outside hole fields: {len(outside)}")
    print(f"Multiply used holes: {len(shared_holes)}")
    print(f"Obscured contacts:   {len(obscured)}")
    print(f"Contact-dot errors:  {len(marker_errors)}")
    print(f"Rubric score:        {score}/4")

    if shared_holes:
        for contacts in shared_holes.values():
            point = contacts[0][2]
            users = ", ".join(
                f"element {element_index} <{tag}>"
                for element_index, tag, _ in contacts
            )
            print(
                f"Hole ({point[0]:g}, {point[1]:g}) is used by {users}.",
                file=sys.stderr,
            )

    for point, element_index, tag in obscured:
        print(
            f"Hole ({point[0]:g}, {point[1]:g}) used by element "
            f"{element_index} <{tag}> is obscured.",
            file=sys.stderr,
        )

    for point, element_index, message in marker_errors:
        print(
            f"Hole ({point[0]:g}, {point[1]:g}) for element "
            f"{element_index}: {message}.",
            file=sys.stderr,
        )

    if score < 4:
        print(
            "Diagram fails: every electrical contact must use its own "
            "pixel-exact visible breadboard hole.",
            file=sys.stderr,
        )
        return 1

    if not endpoints:
        print("PASS: template contract present; no circuit endpoints to check.")
    else:
        print("PASS: every electrical contact is pixel-exact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
