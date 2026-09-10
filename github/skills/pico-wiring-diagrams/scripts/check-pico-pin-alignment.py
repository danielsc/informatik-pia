#!/usr/bin/env python3

import argparse
import math
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class AlignmentParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.breadboard = None
        self.pico = None
        self.pico_pattern = None
        self.pico_pin_circle = None
        self.top_header = None
        self.bottom_header = None
        self.top_terminal_field = None
        self.label_groups = {}
        self.labels = {"top": [], "bottom": []}
        self._active_label_row = None
        self._in_pico_pattern = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        element_id = attributes.get("id")

        if tag == "rect" and element_id == "breadboard":
            self.breadboard = attributes
        elif tag == "rect" and element_id == "pico-top-header":
            self.top_header = attributes
        elif tag == "rect" and element_id == "pico-bottom-header":
            self.bottom_header = attributes
        elif tag == "rect" and element_id == "top-terminal-holes":
            self.top_terminal_field = attributes
        elif tag == "g" and element_id == "pico":
            self.pico = attributes
        elif tag == "g" and attributes.get("aria-label") == (
            "Top Pico header pins 40 through 21"
        ):
            self.label_groups["top"] = attributes
            self._active_label_row = "top"
        elif tag == "g" and attributes.get("aria-label") == (
            "Bottom Pico header pins 1 through 20"
        ):
            self.label_groups["bottom"] = attributes
            self._active_label_row = "bottom"
        elif tag == "pattern" and element_id == "pico-pins":
            self.pico_pattern = attributes
            self._in_pico_pattern = True
        elif tag == "circle" and self._in_pico_pattern:
            if self.pico_pin_circle is None:
                self.pico_pin_circle = attributes
        elif tag == "text" and self._active_label_row:
            classes = attributes.get("class", "").split()
            if "pico-label" in classes:
                self.labels[self._active_label_row].append(attributes)

    def handle_endtag(self, tag):
        if tag == "pattern" and self._in_pico_pattern:
            self._in_pico_pattern = False
        elif tag == "g" and self._active_label_row:
            self._active_label_row = None


def number(attributes, name):
    try:
        return float(attributes[name])
    except (KeyError, ValueError) as error:
        raise ValueError(f"Missing or invalid {name}") from error


def translation_y(transform):
    match = re.fullmatch(
        r"\s*translate\(\s*[-+]?\d+(?:\.\d+)?"
        r"(?:[,\s]+([-+]?\d+(?:\.\d+)?))?\s*\)\s*",
        transform,
    )
    if not match:
        raise ValueError("Pico transform must be a simple translate(x y)")
    return float(match.group(1) or 0)


def matrix(transform):
    match = re.fullmatch(
        r"\s*matrix\(\s*"
        + r"([-.0-9]+)[,\s]+"
        + r"([-.0-9]+)[,\s]+"
        + r"([-.0-9]+)[,\s]+"
        + r"([-.0-9]+)[,\s]+"
        + r"([-.0-9]+)[,\s]+"
        + r"([-.0-9]+)\s*\)\s*",
        transform,
    )
    if not match:
        raise ValueError("Pico label group must use an explicit matrix transform")
    return tuple(float(value) for value in match.groups())


def transformed_point(x, y, values):
    a, b, c, d, e, f = values
    return a * x + c * y + e, b * x + d * y + f


def rotation(attributes):
    match = re.fullmatch(
        r"\s*rotate\(\s*([-.0-9]+)[,\s]+([-.0-9]+)"
        r"[,\s]+([-.0-9]+)\s*\)\s*",
        attributes.get("transform", ""),
    )
    if not match:
        raise ValueError("Pico label must use an explicit rotate transform")
    return tuple(float(value) for value in match.groups())


def distance_to_grid(value, origin, pitch):
    grid_index = round((value - origin) / pitch)
    grid_value = origin + grid_index * pitch
    return abs(value - grid_value)


def centres_in_rect(start, length, origin, pitch):
    first_index = math.ceil((start - origin) / pitch)
    end = start + length
    centres = []
    index = first_index
    while origin + index * pitch < end:
        centre = origin + index * pitch
        if centre >= start:
            centres.append(centre)
        index += 1
    return centres


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
        description="Score Pico header-pad alignment to breadboard holes."
    )
    parser.add_argument("template", type=Path)
    args = parser.parse_args()

    source = args.template.read_text(encoding="utf-8")
    document = AlignmentParser()
    document.feed(source)

    if any(
        item is None
        for item in (
            document.breadboard,
            document.pico,
            document.pico_pattern,
            document.pico_pin_circle,
            document.top_header,
            document.bottom_header,
            document.top_terminal_field,
            document.label_groups.get("top"),
            document.label_groups.get("bottom"),
        )
    ):
        print("Missing breadboard, Pico, or Pico pin-pattern geometry.", file=sys.stderr)
        return 1

    try:
        origin_x = number(document.breadboard, "data-hole-origin-x")
        origin_y = number(document.breadboard, "data-hole-origin-y")
        pitch_x = number(document.breadboard, "data-hole-pitch-x")
        pitch_y = number(document.breadboard, "data-hole-pitch-y")
        first_pin_x = number(document.pico, "data-first-pin-x")
        pin_pitch = number(document.pico, "data-pin-pitch")
        pin_count = int(number(document.pico, "data-pin-count"))
        translate_y = translation_y(document.pico.get("transform", ""))
        top_y = number(document.pico, "data-top-header-y") + translate_y
        bottom_y = number(document.pico, "data-bottom-header-y") + translate_y

        pattern_pitch = number(document.pico_pattern, "width")
        pattern_pitch_y = number(document.pico_pattern, "height")
        pattern_x = number(document.pico_pattern, "x")
        pattern_y = number(document.pico_pattern, "y")
        pattern_circle_x = number(document.pico_pin_circle, "cx")
        pattern_circle_y = number(document.pico_pin_circle, "cy")
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    if pin_count != 20:
        print(f"Expected 20 pins per row, found {pin_count}.", file=sys.stderr)
        return 1

    if not math.isclose(pin_pitch, pitch_x, abs_tol=1e-9):
        print("Pico pin pitch differs from breadboard hole pitch.", file=sys.stderr)
        return 1

    leftmost_terminal_pin_x = (
        origin_x
        + math.ceil(
            (number(document.top_terminal_field, "x") - origin_x) / pitch_x
        )
        * pitch_x
    )
    if not math.isclose(first_pin_x, leftmost_terminal_pin_x, abs_tol=1e-9):
        print(
            "Pico does not begin at the leftmost terminal-field hole.",
            file=sys.stderr,
        )
        return 1

    rendered_pattern_x = pattern_x + pattern_circle_x
    rendered_pattern_y = pattern_y + pattern_circle_y
    top_centres_x = centres_in_rect(
        number(document.top_header, "x"),
        number(document.top_header, "width"),
        rendered_pattern_x,
        pattern_pitch,
    )
    bottom_centres_x = centres_in_rect(
        number(document.bottom_header, "x"),
        number(document.bottom_header, "width"),
        rendered_pattern_x,
        pattern_pitch,
    )
    top_centres_y = centres_in_rect(
        number(document.top_header, "y"),
        number(document.top_header, "height"),
        rendered_pattern_y,
        pattern_pitch_y,
    )
    bottom_centres_y = centres_in_rect(
        number(document.bottom_header, "y"),
        number(document.bottom_header, "height"),
        rendered_pattern_y,
        pattern_pitch_y,
    )

    expected_x = [
        first_pin_x + index * pin_pitch for index in range(pin_count)
    ]
    if top_centres_x != expected_x or bottom_centres_x != expected_x:
        print("Pico metadata disagrees with rendered horizontal pads.", file=sys.stderr)
        return 1

    if top_centres_y != [number(document.pico, "data-top-header-y")]:
        print("Top-header metadata disagrees with rendered pads.", file=sys.stderr)
        return 1

    if bottom_centres_y != [number(document.pico, "data-bottom-header-y")]:
        print("Bottom-header metadata disagrees with rendered pads.", file=sys.stderr)
        return 1

    if len(top_centres_x) != pin_count or len(bottom_centres_x) != pin_count:
        print("Rendered headers do not contain 20 pins each.", file=sys.stderr)
        return 1

    if len(document.labels["top"]) != pin_count or len(
        document.labels["bottom"]
    ) != pin_count:
        print("Expected 20 silkscreen labels on each Pico header.", file=sys.stderr)
        return 1

    try:
        label_x_errors = []
        label_anchor_y = {}
        for row in ("top", "bottom"):
            group = document.label_groups[row]
            if group.get("text-anchor") != ("end" if row == "top" else "start"):
                raise ValueError(f"{row.title()} label anchoring is incorrect")
            transform = matrix(group.get("transform", ""))
            rendered_y = set()
            for index, label in enumerate(document.labels[row]):
                label_x = number(label, "x")
                label_y = number(label, "y")
                angle, pivot_x, pivot_y = rotation(label)
                if (
                    not math.isclose(angle, -90, abs_tol=1e-9)
                    or not math.isclose(pivot_x, label_x, abs_tol=1e-9)
                    or not math.isclose(pivot_y, label_y, abs_tol=1e-9)
                ):
                    raise ValueError(
                        "Every Pico label must read bottom-to-top around its anchor"
                    )
                rendered_x, final_y = transformed_point(
                    label_x, label_y, transform
                )
                label_x_errors.append(abs(rendered_x - expected_x[index]))
                rendered_y.add(final_y)
            if len(rendered_y) != 1:
                raise ValueError(f"{row.title()} labels do not share one anchor line")
            label_anchor_y[row] = rendered_y.pop()
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    maximum_label_x_error = max(label_x_errors)
    top_label_gap = label_anchor_y["top"] - (
        number(document.top_header, "y") + number(document.top_header, "height")
    )
    bottom_label_gap = (
        number(document.bottom_header, "y") - label_anchor_y["bottom"]
    )
    if (
        maximum_label_x_error > 0.5
        or not math.isclose(top_label_gap, 1, abs_tol=1e-9)
        or not math.isclose(bottom_label_gap, 3, abs_tol=1e-9)
    ):
        print(
            "Pico silkscreen labels are not uniformly aligned with their pads.",
            file=sys.stderr,
        )
        return 1

    if not math.isclose(
        distance_to_grid(first_pin_x, rendered_pattern_x, pattern_pitch),
        0.0,
        abs_tol=1e-9,
    ):
        print("Pico metadata disagrees with the rendered pin pattern.", file=sys.stderr)
        return 1

    x_errors = [
        distance_to_grid(first_pin_x + index * pin_pitch, origin_x, pitch_x)
        for index in range(pin_count)
    ]
    y_errors = [
        distance_to_grid(top_y, origin_y, pitch_y),
        distance_to_grid(bottom_y, origin_y, pitch_y),
    ]
    max_x_error = max(x_errors)
    max_y_error = max(y_errors)
    maximum_error = max(max_x_error, max_y_error)
    score = score_error(maximum_error)

    print(f"Pins checked:       {pin_count * 2}")
    print(f"Maximum X error:    {max_x_error:.2f}px")
    print(f"Maximum Y error:    {max_y_error:.2f}px")
    print(f"Label X error:      {maximum_label_x_error:.2f}px")
    print(f"Top label gap:      {top_label_gap:.2f}px")
    print(f"Bottom label gap:   {bottom_label_gap:.2f}px")
    print(f"Rubric score:       {score}/4")

    if score < 4:
        print(
            "Template fails: every Pico pin must align to the pixel.",
            file=sys.stderr,
        )
        return 1

    print("PASS: all 40 Pico pins align exactly with breadboard holes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
