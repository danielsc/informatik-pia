#!/usr/bin/env python3

import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class GeometryParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.breadboard = None
        self.pico = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        element_id = attributes.get("id")
        if tag == "rect" and element_id == "breadboard":
            self.breadboard = attributes
        elif tag == "g" and element_id == "pico":
            self.pico = attributes


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


def score_offset(offset):
    if offset <= 4:
        return 4
    if offset <= 13.5:
        return 3
    if offset <= 27:
        return 2
    if offset <= 54:
        return 1
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Score vertical Pico centring in the wiring template."
    )
    parser.add_argument("template", type=Path)
    args = parser.parse_args()

    source = args.template.read_text(encoding="utf-8")
    document = GeometryParser()
    document.feed(source)

    if document.breadboard is None or document.pico is None:
        print("Missing #breadboard rectangle or #pico group.", file=sys.stderr)
        return 1

    try:
        breadboard_center = (
            number(document.breadboard, "y")
            + number(document.breadboard, "height") / 2
        )
        pico_center = (
            number(document.pico, "data-bounds-y")
            + translation_y(document.pico.get("transform", ""))
            + number(document.pico, "data-bounds-height") / 2
        )
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    offset = abs(breadboard_center - pico_center)
    score = score_offset(offset)

    print(f"Breadboard centre: {breadboard_center:.1f}px")
    print(f"Pico centre:       {pico_center:.1f}px")
    print(f"Vertical offset:   {offset:.1f}px")
    print(f"Rubric score:      {score}/4")

    if score < 4:
        print("Template fails: the reusable Pico must score 4/4.", file=sys.stderr)
        return 1

    print("PASS: Pico is vertically centred in the breadboard template.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

