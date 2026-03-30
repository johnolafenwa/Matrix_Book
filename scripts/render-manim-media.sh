#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCENES_FILE="$ROOT/media/manim_scenes.py"
MEDIA_DIR="$ROOT/output/manim-build"
DEST_DIR="$ROOT/public/media/animations"
VENV="$ROOT/.venv-media/bin/activate"

if [[ ! -f "$VENV" ]]; then
  echo "Missing media virtualenv at $VENV" >&2
  exit 1
fi

mkdir -p "$DEST_DIR"
rm -rf "$MEDIA_DIR"

source "$VENV"

render_scene() {
  local scene_name="$1"
  local output_name="$2"

  manim -ql --media_dir "$MEDIA_DIR" "$SCENES_FILE" "$scene_name" >/dev/null
  local rendered
  rendered="$(find "$MEDIA_DIR/videos/manim_scenes" -name "${scene_name}.mp4" | head -n 1)"
  if [[ -z "$rendered" ]]; then
    echo "Could not find rendered file for $scene_name" >&2
    exit 1
  fi
  cp "$rendered" "$DEST_DIR/$output_name"
}

render_scene "BasisVectorsTransform" "ch05-basis-vectors-transform.mp4"
render_scene "DeterminantAreaScale" "ch06-determinant-area-scale.mp4"
render_scene "LeastSquaresProjection" "ch09-least-squares-projection.mp4"
render_scene "EigenvectorDirections" "ch10-eigenvector-directions.mp4"
render_scene "SVDRotateStretchRotate" "ch13-svd-rotate-stretch-rotate.mp4"

echo "Rendered Manim assets into $DEST_DIR"
