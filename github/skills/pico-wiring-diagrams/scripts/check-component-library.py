#!/usr/bin/env python3

import argparse
import math
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


REQUIRED_COMPONENTS = {
    "component-pico",
    "component-led-5mm-red",
    "component-button-6mm",
    "component-resistor-220",
    "component-resistor-1k",
    "component-resistor-2k",
    "component-resistor-10k",
    "component-potentiometer",
    "component-rgb8-module",
    "component-passive-buzzer",
    "component-s8050",
    "component-hcsr04",
}


class ComponentParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.svg_attributes = {}
        self.symbols = set()
        self.symbol_attributes = {}
        self.uses = set()
        self.use_attributes = []
        self._active_symbol = None
        self.pico_labels = 0

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        self.tags.append(tag)
        if tag == "svg" and not self.svg_attributes:
            self.svg_attributes = attributes
        elif tag == "symbol" and attributes.get("id"):
            symbol_id = attributes["id"]
            self.symbols.add(symbol_id)
            self.symbol_attributes[symbol_id] = attributes
            self._active_symbol = symbol_id
        elif tag == "use":
            href = attributes.get("href", "")
            if href.startswith("#"):
                self.uses.add(href[1:])
                self.use_attributes.append(attributes)
        elif (
            tag == "text"
            and self._active_symbol == "component-pico"
            and "pico-label" in attributes.get("class", "").split()
        ):
            self.pico_labels += 1

    def handle_endtag(self, tag):
        if tag == "symbol":
            self._active_symbol = None


def main():
    parser = argparse.ArgumentParser(
        description="Check the Pico workshop SVG component gallery."
    )
    parser.add_argument("gallery", type=Path)
    args = parser.parse_args()

    source = args.gallery.read_text(encoding="utf-8")
    document = ComponentParser()
    document.feed(source)

    missing = sorted(REQUIRED_COMPONENTS - document.symbols)
    unused = sorted(REQUIRED_COMPONENTS - document.uses)
    pico = document.symbol_attributes.get("component-pico", {})
    rgb = document.symbol_attributes.get("component-rgb8-module", {})
    resistor_ids = {
        "component-resistor-220",
        "component-resistor-1k",
        "component-resistor-2k",
        "component-resistor-10k",
    }
    resistor_symbols_are_canonical = all(
        document.symbol_attributes.get(component_id, {}).get("viewbox")
        == "0 0 104 24"
        and document.symbol_attributes.get(component_id, {}).get("data-width")
        == "104"
        and document.symbol_attributes.get(component_id, {}).get("data-height")
        == "24"
        and document.symbol_attributes.get(component_id, {}).get(
            "data-body-hole-span"
        )
        == "2"
        and document.symbol_attributes.get(component_id, {}).get(
            "data-lead-hole-span"
        )
        == "1"
        and document.symbol_attributes.get(component_id, {}).get(
            "data-total-hole-span"
        )
        == "4"
        for component_id in resistor_ids
    )
    resistor_previews_are_unscaled = all(
        attributes.get("width") == "104"
        and attributes.get("height") == "24"
        for attributes in document.use_attributes
        if attributes.get("href", "")[1:] in resistor_ids
    )
    all_previews_are_unscaled = True
    for attributes in document.use_attributes:
        component_id = attributes.get("href", "")[1:]
        symbol = document.symbol_attributes.get(component_id)
        if not component_id.startswith("component-") or symbol is None:
            continue
        values = [
            float(value)
            for value in re.split(r"[\s,]+", symbol.get("viewbox", "").strip())
            if value
        ]
        try:
            width = float(attributes["width"])
            height = float(attributes["height"])
        except (KeyError, ValueError):
            all_previews_are_unscaled = False
            break
        if len(values) != 4 or not (
            math.isclose(width, values[2], abs_tol=1e-9)
            and math.isclose(height, values[3], abs_tol=1e-9)
        ):
            all_previews_are_unscaled = False
            break
    checks = {
        "HTML5 doctype": source.lstrip().lower().startswith("<!doctype html>"),
        "one inline SVG": document.tags.count("svg") == 1,
        "responsive viewBox": "viewbox" in document.svg_attributes,
        "accessible SVG": (
            document.svg_attributes.get("role") == "img"
            and bool(document.svg_attributes.get("aria-labelledby"))
            and "title" in document.tags
            and "desc" in document.tags
        ),
        "print stylesheet": "@media print" in source,
        "no canvas": "canvas" not in document.tags,
        "no external images": "img" not in document.tags,
        "all required symbols": not missing,
        "all required previews": not unused,
        "canonical Pico dimensions": (
            pico.get("viewbox") == "78 195 520 192"
            and pico.get("data-width") == "520"
            and pico.get("data-height") == "192"
            and pico.get("data-pin-count") == "40"
        ),
        "all Pico labels": document.pico_labels == 40,
        "physical RGB module": (
            rgb.get("viewbox") == "0 0 220 220"
            and rgb.get("data-shape") == "square"
            and rgb.get("data-pixel-count") == "8"
            and rgb.get("data-mounting-holes") == "4"
            and rgb.get("data-headers") == "IN,OUT"
        ),
        "canonical resistor span": resistor_symbols_are_canonical,
        "unscaled resistor previews": resistor_previews_are_unscaled,
        "all previews at canonical scale": all_previews_are_unscaled,
    }

    for name, passed in checks.items():
        print(("PASS" if passed else "FAIL") + "  " + name)
    if missing:
        print("Missing symbols: " + ", ".join(missing), file=sys.stderr)
    if unused:
        print("Missing previews: " + ", ".join(unused), file=sys.stderr)
    if not all(checks.values()):
        return 1
    print(f"\nPASS: all {len(REQUIRED_COMPONENTS)} workshop components are defined and shown.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
