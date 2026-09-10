#!/usr/bin/env python3

import argparse
import math
import sys
from html.parser import HTMLParser
from pathlib import Path


class FootprintParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.breadboard = None
        self.pico = None
        self.pico_board = None
        self.clip_rect = None
        self._in_footprint_clip = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        element_id = attributes.get("id")
        if tag == "rect" and element_id == "breadboard":
            self.breadboard = attributes
        elif tag == "g" and element_id == "pico":
            self.pico = attributes
        elif tag == "rect" and element_id == "pico-board":
            self.pico_board = attributes
        elif tag == "clippath" and element_id == "pico-footprint-clip":
            self._in_footprint_clip = True
        elif tag == "rect" and self._in_footprint_clip:
            self.clip_rect = attributes

    def handle_endtag(self, tag):
        if tag == "clippath" and self._in_footprint_clip:
            self._in_footprint_clip = False


def number(attributes, name):
    try:
        return float(attributes[name])
    except (KeyError, ValueError) as error:
        raise ValueError(f"Missing or invalid {name}") from error


def same(a, b):
    return math.isclose(a, b, abs_tol=1e-9)


def score_overflow(overflow, pitch):
    if same(overflow, 0):
        return 4
    if overflow <= 0.5:
        return 3
    if overflow <= 2:
        return 2
    if overflow <= pitch:
        return 1
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Check the Pico drawing against its maximum footprint."
    )
    parser.add_argument("template", type=Path)
    args = parser.parse_args()

    source = args.template.read_text(encoding="utf-8")
    document = FootprintParser()
    document.feed(source)

    if any(
        value is None
        for value in (
            document.breadboard,
            document.pico,
            document.pico_board,
            document.clip_rect,
        )
    ):
        print("Missing breadboard, Pico, board, or clip geometry.", file=sys.stderr)
        return 1

    try:
        pitch_x = number(document.breadboard, "data-hole-pitch-x")
        pitch_y = number(document.breadboard, "data-hole-pitch-y")
        columns = number(document.pico, "data-footprint-columns")
        row_pitches = number(document.pico, "data-footprint-row-pitches")
        channel_height = number(document.pico, "data-footprint-channel-height")
        first_pin_x = number(document.pico, "data-first-pin-x")
        pin_pitch = number(document.pico, "data-pin-pitch")
        pin_count = int(number(document.pico, "data-pin-count"))
        top_header_y = number(document.pico, "data-top-header-y")
        bottom_header_y = number(document.pico, "data-bottom-header-y")
        bounds = {
            key: number(document.pico, f"data-bounds-{key}")
            for key in ("x", "y", "width", "height")
        }
        clip = {
            key: number(document.clip_rect, key)
            for key in ("x", "y", "width", "height")
        }
        board = {
            key: number(document.pico_board, key)
            for key in ("x", "y", "width", "height")
        }
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1

    maximum_width = columns * pitch_x
    maximum_height = row_pitches * pitch_y + channel_height
    overflow_x = max(0.0, bounds["width"] - maximum_width)
    overflow_y = max(0.0, bounds["height"] - maximum_height)
    maximum_overflow = max(overflow_x, overflow_y)

    if any(not same(bounds[key], clip[key]) for key in bounds):
        print("Declared Pico bounds disagree with the clip rectangle.", file=sys.stderr)
        return 1

    board_is_contained = (
        board["x"] >= bounds["x"]
        and board["y"] >= bounds["y"]
        and board["x"] + board["width"] <= bounds["x"] + bounds["width"]
        and board["y"] + board["height"] <= bounds["y"] + bounds["height"]
    )
    if not board_is_contained:
        print("Green Pico board exceeds the declared footprint.", file=sys.stderr)
        return 1

    header_center_x = first_pin_x + (pin_count - 1) * pin_pitch / 2
    header_center_y = (top_header_y + bottom_header_y) / 2
    board_center_x = board["x"] + board["width"] / 2
    board_center_y = board["y"] + board["height"] / 2
    if not same(board_center_x, header_center_x) or not same(
        board_center_y, header_center_y
    ):
        print("Green Pico board is shifted relative to its header pads.", file=sys.stderr)
        return 1

    if document.pico.get("clip-path") != "url(#pico-footprint-clip)":
        print("Pico group does not enforce the footprint clip.", file=sys.stderr)
        return 1

    score = score_overflow(maximum_overflow, max(pitch_x, pitch_y))
    print(f"Maximum width:      {maximum_width:.2f}px")
    print(f"Pico width:         {bounds['width']:.2f}px")
    print(f"Green PCB width:    {board['width']:.2f}px")
    print(f"Maximum height:     {maximum_height:.2f}px")
    print(f"Pico height:        {bounds['height']:.2f}px")
    print(f"Green PCB height:   {board['height']:.2f}px")
    print(f"PCB/pad offset X:   {abs(board_center_x - header_center_x):.2f}px")
    print(f"PCB/pad offset Y:   {abs(board_center_y - header_center_y):.2f}px")
    print(f"Maximum overflow:   {maximum_overflow:.2f}px")
    print(f"Rubric score:       {score}/4")

    if score < 4:
        print("Template fails: Pico exceeds its exact footprint.", file=sys.stderr)
        return 1

    print("PASS: the complete Pico drawing is clipped to the exact footprint.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
