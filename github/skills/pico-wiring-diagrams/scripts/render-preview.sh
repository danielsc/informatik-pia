#!/usr/bin/env bash
set -eu

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
  echo "Usage: bash render-preview.sh DIAGRAM.html [OUTPUT.png|OUTPUT_DIRECTORY]" >&2
  exit 2
fi

input=$1
destination=${2:-"${TMPDIR:-/tmp}/pico-wiring-preview"}

if [ ! -f "$input" ]; then
  echo "Diagram not found: $input" >&2
  exit 1
fi

case "$destination" in
  *.png)
    output=$destination
    output_dir=$(dirname "$output")
    ;;
  *)
    output_dir=$destination
    output="$output_dir/$(basename "$input" .html).png"
    ;;
esac

mkdir -p "$output_dir"

for browser in \
  chromium \
  chromium-browser \
  google-chrome \
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
do
  if command -v "$browser" >/dev/null 2>&1 || [ -x "$browser" ]; then
    screenshot_output="$(cd "$output_dir" && pwd)/$(basename "$output")"
    if "$browser" \
      --headless=new \
      --disable-gpu \
      --hide-scrollbars \
      --window-size=1600,1600 \
      --force-device-scale-factor=1 \
      --screenshot="$screenshot_output" \
      "file://$(cd "$(dirname "$input")" && pwd)/$(basename "$input")" \
      >/dev/null 2>&1
    then
      echo "$output"
      exit 0
    fi
  fi
done

if command -v qlmanage >/dev/null 2>&1; then
  qlmanage -r cache >/dev/null 2>&1
  qlmanage -t -s 1600 -o "$output_dir" "$input" >/dev/null 2>&1
  generated="$output_dir/$(basename "$input").png"
  if [ "$generated" != "$output" ]; then
    mv "$generated" "$output"
  fi
  echo "$output"
  exit 0
fi

echo "No supported renderer found. Open the HTML file in a browser." >&2
exit 1
