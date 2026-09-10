#!/usr/bin/env python3

import argparse
import itertools
import math
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class RoutingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self._connections_depth = 0
        self.routes = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "g" and attributes.get("id") == "circuit-connections":
            self._connections_depth = 1
            return
        if self._connections_depth and tag == "g":
            self._connections_depth += 1
        if (
            self._connections_depth
            and tag in {"line", "polyline"}
            and "data-connection-kind" in attributes
        ):
            self.routes.append((tag, attributes))

    def handle_endtag(self, tag):
        if tag == "g" and self._connections_depth:
            self._connections_depth -= 1


def number(attributes, name):
    try:
        return float(attributes[name])
    except (KeyError, ValueError) as error:
        raise ValueError(f"Missing or invalid {name}") from error


def points(tag, attributes):
    if tag == "line":
        return [
            (number(attributes, "x1"), number(attributes, "y1")),
            (number(attributes, "x2"), number(attributes, "y2")),
        ]
    values = [
        float(item)
        for item in re.split(r"[\s,]+", attributes.get("points", "").strip())
        if item
    ]
    if len(values) < 4 or len(values) % 2:
        raise ValueError("Polyline points must contain at least two X,Y pairs")
    return list(zip(values[0::2], values[1::2]))


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def same_point(a, b):
    return math.isclose(a[0], b[0], abs_tol=1e-9) and math.isclose(
        a[1], b[1], abs_tol=1e-9
    )


def between(value, end_a, end_b):
    return min(end_a, end_b) - 1e-9 <= value <= max(end_a, end_b) + 1e-9


def on_segment(a, b, point):
    return (
        math.isclose(cross(a, b, point), 0, abs_tol=1e-9)
        and between(point[0], a[0], b[0])
        and between(point[1], a[1], b[1])
    )


def invalid_intersection(first, second):
    a, b = first
    c, d = second
    if not (
        on_segment(a, b, c)
        or on_segment(a, b, d)
        or on_segment(c, d, a)
        or on_segment(c, d, b)
    ):
        ab_c = cross(a, b, c)
        ab_d = cross(a, b, d)
        cd_a = cross(c, d, a)
        cd_b = cross(c, d, b)
        return (ab_c > 0) != (ab_d > 0) and (cd_a > 0) != (cd_b > 0)

    shared_endpoints = [
        point
        for point in (a, b)
        if any(same_point(point, other) for other in (c, d))
    ]
    if shared_endpoints:
        collinear = math.isclose(cross(a, b, c), 0, abs_tol=1e-9) and math.isclose(
            cross(a, b, d), 0, abs_tol=1e-9
        )
        if not collinear:
            return False
        axis = 0 if abs(a[0] - b[0]) >= abs(a[1] - b[1]) else 1
        overlap = min(max(a[axis], b[axis]), max(c[axis], d[axis])) - max(
            min(a[axis], b[axis]), min(c[axis], d[axis])
        )
        return overlap > 1e-9

    return any(
        on_segment(a, b, point) for point in (c, d)
    ) or any(on_segment(c, d, point) for point in (a, b))


def main():
    parser = argparse.ArgumentParser(
        description="Reject overlaps and ambiguous crossings in circuit routes."
    )
    parser.add_argument("diagram", type=Path)
    args = parser.parse_args()

    document = RoutingParser()
    document.feed(args.diagram.read_text(encoding="utf-8"))

    try:
        routes = []
        for route_index, (tag, attributes) in enumerate(document.routes, start=1):
            route_points = points(tag, attributes)
            for segment_index in range(len(route_points) - 1):
                routes.append(
                    (
                        route_index,
                        segment_index + 1,
                        (route_points[segment_index], route_points[segment_index + 1]),
                    )
                )
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    conflicts = []
    for first, second in itertools.combinations(routes, 2):
        if first[0] == second[0]:
            continue
        if invalid_intersection(first[2], second[2]):
            conflicts.append((first[:2], second[:2]))

    print(f"Electrical routes:  {len(document.routes)}")
    print(f"Segments checked:   {len(routes)}")
    print(f"Routing conflicts:  {len(conflicts)}")
    if conflicts:
        for first, second in conflicts:
            print(
                f"Conflict: route {first[0]} segment {first[1]} and "
                f"route {second[0]} segment {second[1]}",
                file=sys.stderr,
            )
        return 1

    print("PASS: no conductors overlap or cross ambiguously.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
