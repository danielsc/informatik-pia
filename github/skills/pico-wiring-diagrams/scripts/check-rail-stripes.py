#!/usr/bin/env python3

import argparse
import math
import sys
from html.parser import HTMLParser
from pathlib import Path


class RailParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.breadboard = None
        self.fields = {}
        self.stripes = {}

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        element_id = attributes.get("id")
        if tag == "rect" and element_id == "breadboard":
            self.breadboard = attributes
        elif tag == "rect" and element_id in {
            "top-power-rail-holes",
            "bottom-power-rail-holes",
        }:
            self.fields[element_id] = attributes
        elif tag == "line" and element_id in {
            "top-rail-upper-stripe",
            "top-rail-lower-stripe",
            "bottom-rail-upper-stripe",
            "bottom-rail-lower-stripe",
        }:
            self.stripes[element_id] = attributes


def number(attributes, name):
    try:
        return float(attributes[name])
    except (KeyError, ValueError) as error:
        raise ValueError(f"Missing or invalid {name}") from error


def hole_centres(field, origin, pitch):
    start = number(field, "y")
    end = start + number(field, "height")
    first_index = math.ceil((start - origin) / pitch)
    centres = []
    index = first_index
    while origin + index * pitch < end:
        centres.append(origin + index * pitch)
        index += 1
    return centres


def main():
    parser = argparse.ArgumentParser(
        description="Check symmetric power-rail stripe placement."
    )
    parser.add_argument("diagram", type=Path)
    args = parser.parse_args()

    document = RailParser()
    document.feed(args.diagram.read_text(encoding="utf-8"))
    if (
        document.breadboard is None
        or len(document.fields) != 2
        or len(document.stripes) != 4
    ):
        print("Missing breadboard, rail fields, or rail stripes.", file=sys.stderr)
        return 1

    try:
        origin = number(document.breadboard, "data-hole-origin-y")
        pitch = number(document.breadboard, "data-hole-pitch-y")
        errors = []
        distances = []
        for bank in ("top", "bottom"):
            centres = hole_centres(
                document.fields[f"{bank}-power-rail-holes"], origin, pitch
            )
            if len(centres) != 2:
                raise ValueError(f"{bank.title()} rail must contain two hole rows")
            upper_y = number(document.stripes[f"{bank}-rail-upper-stripe"], "y1")
            lower_y = number(document.stripes[f"{bank}-rail-lower-stripe"], "y1")
            field_y = number(
                document.fields[f"{bank}-power-rail-holes"], "y"
            )
            field_end = field_y + number(
                document.fields[f"{bank}-power-rail-holes"], "height"
            )
            if not math.isclose(field_y, upper_y, abs_tol=1e-9) or not math.isclose(
                field_end, lower_y, abs_tol=1e-9
            ):
                raise ValueError(
                    f"{bank.title()} rail hole field must end at its two stripes"
                )
            if not math.isclose(
                upper_y,
                number(document.stripes[f"{bank}-rail-upper-stripe"], "y2"),
                abs_tol=1e-9,
            ) or not math.isclose(
                lower_y,
                number(document.stripes[f"{bank}-rail-lower-stripe"], "y2"),
                abs_tol=1e-9,
            ):
                raise ValueError("Rail stripes must be horizontal")
            upper_distance = centres[0] - upper_y
            lower_distance = lower_y - centres[1]
            distances.extend((upper_distance, lower_distance))
            errors.extend(
                (
                    abs(upper_distance - pitch / 2),
                    abs(lower_distance - pitch / 2),
                )
            )
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    maximum_error = max(errors)
    print("Stripe distances:   " + ", ".join(f"{value:.2f}px" for value in distances))
    print(f"Expected distance:  {pitch / 2:.2f}px")
    print(f"Maximum error:      {maximum_error:.2f}px")
    if not math.isclose(maximum_error, 0, abs_tol=1e-9):
        print("FAIL: rail stripes do not frame the pins symmetrically.", file=sys.stderr)
        return 1
    print("PASS: top and bottom rail stripes frame their pins identically.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
