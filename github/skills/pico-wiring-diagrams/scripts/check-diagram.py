#!/usr/bin/env python3

import argparse
import sys
from html.parser import HTMLParser
from pathlib import Path


class DiagramParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.svg_attributes = {}

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if tag == "svg" and not self.svg_attributes:
            self.svg_attributes = dict(attrs)


def main():
    parser = argparse.ArgumentParser(
        description="Check the required structure of a Pico HTML/SVG diagram."
    )
    parser.add_argument("diagram", type=Path)
    args = parser.parse_args()

    source = args.diagram.read_text(encoding="utf-8")
    document = DiagramParser()
    document.feed(source)

    checks = {
        "HTML5 doctype": source.lstrip().lower().startswith("<!doctype html>"),
        "one inline SVG": document.tags.count("svg") == 1,
        "SVG image role": document.svg_attributes.get("role") == "img",
        "SVG aria-labelledby": bool(
            document.svg_attributes.get("aria-labelledby")
        ),
        "SVG title": "title" in document.tags,
        "SVG description": "desc" in document.tags,
        "figure caption": "figcaption" in document.tags,
        "exact connection table": (
            "table" in document.tags and "Exact connection list" in source
        ),
        "print stylesheet": "@media print" in source,
        "responsive viewBox": "viewbox" in document.svg_attributes,
        "no canvas": "canvas" not in document.tags,
        "no unresolved template markers": "REPLACE" not in source,
    }

    failed = [name for name, passed in checks.items() if not passed]
    for name, passed in checks.items():
        print(("PASS" if passed else "FAIL") + "  " + name)

    if failed:
        print("\nStructural check failed: " + ", ".join(failed), file=sys.stderr)
        return 1

    print("\nStructural checks passed.")
    print("Electrical correctness and visual quality still require rubric review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
