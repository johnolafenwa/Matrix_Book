# The Matrix Book

An intuitive, visual, and practical guide to matrices.

Matrices are one of the main languages of modern mathematics, science, engineering, graphics, economics, and machine learning. They organize data, describe transformations, solve systems, encode networks, and reveal structure inside complicated problems. This book is designed to make matrices feel concrete before they feel abstract.

The goal is not only to show you how matrix methods work, but also to help you *see* what they mean. Throughout the book, matrices are treated in several complementary ways:

- as tables of numbers
- as machines that transform vectors
- as maps between coordinate systems
- as summaries of relationships in data
- as tools for solving large real-world problems

## How This Book Is Organized

The book moves from intuition to formalism, then from core techniques to major applications.

- The early chapters build the basic language: rows, columns, operations, systems, and geometric meaning.
- The middle chapters introduce the central structural ideas of linear algebra: determinants, inverses, subspaces, orthogonality, eigenvalues, and decomposition.
- The later chapters show why these ideas matter in practice: networks, data, image processing, machine learning, differential equations, and scientific computing.

Each chapter aims to be readable on its own, but the book works best in order.

## What Makes This Book Visual

To keep the ideas accessible, the chapters use:

- Mermaid diagrams for transformations, flows, and concept maps
- tables and worked examples for concrete computation
- geometric interpretations whenever a concept has a shape-based meaning
- analogies that connect abstract ideas to familiar mental models
- recap sections, common mistakes, and exercises for consolidation

## Suggested Reading Paths

If you want a full foundation, read everything in order.

If you are here mainly for applications:

- For graphics and geometry, focus on Chapters 3, 5, 6, 10, 11, and 13.
- For data science and machine learning, focus on Chapters 8, 9, 10, 12, 13, and 15.
- For dynamical systems, focus on Chapters 10, 11, 14, and 16.
- For scientific computing, focus on Chapters 4, 7, 9, 13, and 17.

## Table Of Contents

### Part I. Seeing Matrices

1. [Why Matrices Matter](./chapters/01-why-matrices-matter.md)  
   Why matrices appear everywhere, and how to think of them as tables, machines, and maps.

2. [Seeing Matrices](./chapters/02-seeing-matrices.md)  
   Rows, columns, dimensions, vectors, and the different ways a single matrix can be interpreted.

3. [Matrix Operations](./chapters/03-matrix-operations.md)  
   Addition, scaling, multiplication, transpose, and what these operations mean.

4. [Solving Systems](./chapters/04-solving-systems.md)  
   Gaussian elimination, pivots, augmented matrices, and the logic of solving many equations at once.

### Part II. Geometry And Structure

5. [Linear Transformations And Geometry](./chapters/05-linear-transformations-and-geometry.md)  
   Stretching, rotating, shearing, and understanding matrices through movement in space.

6. [Determinants](./chapters/06-determinants.md)  
   Signed area, signed volume, orientation, invertibility, and why determinants measure scaling.

7. [Inverses And Factorizations](./chapters/07-inverses-and-factorizations.md)  
   Undoing transformations, solving efficiently, and breaking matrices into simpler pieces.

8. [Subspaces, Basis, And Rank](./chapters/08-subspaces-basis-rank.md)  
   Span, linear independence, column space, null space, dimension, and rank.

### Part III. Direction, Approximation, And Decomposition

9. [Orthogonality And Least Squares](./chapters/09-orthogonality-and-least-squares.md)  
   Dot products, projections, orthonormal bases, and fitting imperfect data.

10. [Eigenvalues And Eigenvectors](./chapters/10-eigenvalues-and-eigenvectors.md)  
    Invariant directions, scaling factors, and why some directions matter more than others.

11. [Diagonalization And Dynamics](./chapters/11-diagonalization-and-dynamics.md)  
    Repeated matrix action, powers of matrices, and discrete-time systems.

12. [Symmetric Matrices And Quadratic Forms](./chapters/12-symmetric-matrices-and-quadratic-forms.md)  
    Energy, curvature, ellipses, principal axes, and why symmetry simplifies everything.

13. [Singular Value Decomposition](./chapters/13-singular-value-decomposition.md)  
    Rotate, stretch, rotate again: the geometry and power of SVD.

### Part IV. Applications And Computation

14. [Matrices In Networks And Markov Chains](./chapters/14-matrices-in-networks-and-markov-chains.md)  
    Graphs, transitions, walks, steady states, and long-run behavior.

15. [Matrices In Data, Images, And Machine Learning](./chapters/15-matrices-in-data-images-and-ml.md)  
    Datasets, features, image grids, embeddings, covariance intuition, and practical modeling ideas.

16. [Differential Equations And Continuous Systems](./chapters/16-differential-equations-and-continuous-systems.md)  
    Coupled systems, matrix exponentials, and continuous-time dynamics.

17. [Numerical Linear Algebra](./chapters/17-numerical-linear-algebra.md)  
    Floating point arithmetic, conditioning, algorithmic stability, and the computational reality of matrix problems.

18. [Cheat Sheet And Next Steps](./chapters/18-cheat-sheet-and-next-steps.md)  
    A synthesis chapter with concept links, common pitfalls, and directions for further study.

### Appendices

A. [Guided Problems And Mini-Solutions](./chapters/appendix-a-guided-problems-and-mini-solutions.md)  
   A worked-practice appendix that shows how to attack representative matrix problems step by step.

B. [Visual Glossary And Symbol Guide](./chapters/appendix-b-visual-glossary-and-symbol-guide.md)  
   A notation guide, concept dictionary, and translation map between algebraic, geometric, and applied viewpoints.

## Who This Book Is For

This book is for:

- self-learners who want intuition before abstraction
- students taking a first course in linear algebra
- engineers and programmers who use matrices in practice
- readers who know some algebra but want deeper geometric understanding

You do not need advanced prerequisites. Comfort with basic algebra is enough to begin.

## A Note On Style

The book deliberately revisits the same ideas from several angles. That is not repetition for its own sake. Matrices become easier once you stop trying to force a single interpretation on them. A matrix can be a calculator, a camera move, a network summary, a data table, or a system of relationships. The same object keeps revealing new meanings as your understanding deepens.

## Attribution

**Authors:** John Olafenwa and GPT-5.4

This book was created for personal learning by John Olafenwa, using the OpenAI Codex App powered by GPT-5.4.

Suggested citation:

> John Olafenwa and GPT-5.4. *The Matrix Book: A Visual Guide to Matrices*. 2026. Personal learning edition created using the OpenAI Codex App powered by GPT-5.4.

Project and contact links:

- Website: [matrix.johnolafenwa.com](https://matrix.johnolafenwa.com)
- Repository: [github.com/johnolafenwa/Matrix_Book](https://github.com/johnolafenwa/Matrix_Book)
- X / Twitter: [@johnolafenwa](https://x.com/johnolafenwa)
- LinkedIn: [John Olafenwa](https://www.linkedin.com/in/olafenwajohn/)
- Email: [johnolafenwa@gmail.com](mailto:johnolafenwa@gmail.com)

## Start Reading

Begin with [Chapter 1](./chapters/01-why-matrices-matter.md).

## Local Build

This repository also includes a polished web-book build powered by VitePress.

- Install dependencies: `npm install`
- Start the local reading edition: `npm run dev`
- Build the static site and manuscript: `npm run build`
- Preview the built site: `npm run preview`

Build outputs:

- `dist/` contains the static book site
- `dist/book-manuscript.md` contains a combined manuscript assembled from the chapter files
