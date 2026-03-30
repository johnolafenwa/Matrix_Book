# Book Media

This directory contains the source files and notes for the richer media used in the book build.

## First Batch

- `manim_scenes.py` defines five animated scenes:
  - Chapter 5: basis vectors under a transformation
  - Chapter 6: determinant as area scaling
  - Chapter 9: least squares as projection
  - Chapter 10: eigenvectors staying on their lines
  - Chapter 13: SVD as rotate, stretch, rotate
- Three conceptual illustrations were generated and published under `public/media/illustrations/`:
  - Chapter 1: real-world matrix applications collage
  - Chapter 12: quadratic-form landscape
  - Chapter 14: network city / transit map

## Rendering

Use:

```bash
./scripts/render-manim-media.sh
```

This writes final `.mp4` files to `public/media/animations/` and keeps Manim intermediates under `output/manim-build/`.

The static illustrations were generated with the `imagegen` skill and are also stored in `output/imagegen/` before being copied into `public/media/illustrations/`.
