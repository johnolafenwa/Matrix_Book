export const book = {
  title: "The Matrix Book",
  shortTitle: "Matrix Book",
  subtitle: "An intuitive, visual, and practical guide to matrices",
  description:
    "A visual-first linear algebra book that moves from tables and transformations to eigenvalues, SVD, networks, data, and dynamics.",
  parts: [
    {
      title: "Part I. Seeing Matrices",
      summary:
        "Build the language of matrices from intuition, shape, operations, and systems.",
      items: [
        {
          text: "Chapter 1. Why Matrices Matter",
          link: "/chapters/01-why-matrices-matter",
          file: "chapters/01-why-matrices-matter.md",
          description:
            "Why matrices appear everywhere, and how to think of them as tables, machines, and maps."
        },
        {
          text: "Chapter 2. Seeing Matrices",
          link: "/chapters/02-seeing-matrices",
          file: "chapters/02-seeing-matrices.md",
          description:
            "Rows, columns, dimensions, vectors, and the different ways a matrix can be read."
        },
        {
          text: "Chapter 3. Matrix Operations",
          link: "/chapters/03-matrix-operations",
          file: "chapters/03-matrix-operations.md",
          description:
            "Addition, scaling, multiplication, transpose, and the meaning behind the rules."
        },
        {
          text: "Chapter 4. Solving Systems",
          link: "/chapters/04-solving-systems",
          file: "chapters/04-solving-systems.md",
          description:
            "Gaussian elimination, pivots, augmented matrices, and the logic of solving many equations at once."
        }
      ]
    },
    {
      title: "Part II. Geometry and Structure",
      summary:
        "Move from calculation into geometry, structure, invertibility, and the hidden shape inside matrices.",
      items: [
        {
          text: "Chapter 5. Linear Transformations and Geometry",
          link: "/chapters/05-linear-transformations-and-geometry",
          file: "chapters/05-linear-transformations-and-geometry.md",
          description:
            "Stretching, rotating, shearing, and understanding matrices through movement in space."
        },
        {
          text: "Chapter 6. Determinants",
          link: "/chapters/06-determinants",
          file: "chapters/06-determinants.md",
          description:
            "Signed area, signed volume, orientation, invertibility, and why determinants measure scaling."
        },
        {
          text: "Chapter 7. Inverses and Factorizations",
          link: "/chapters/07-inverses-and-factorizations",
          file: "chapters/07-inverses-and-factorizations.md",
          description:
            "Undoing transformations, solving efficiently, and breaking matrices into simpler pieces."
        },
        {
          text: "Chapter 8. Subspaces, Basis, and Rank",
          link: "/chapters/08-subspaces-basis-rank",
          file: "chapters/08-subspaces-basis-rank.md",
          description:
            "Span, independence, column space, null space, dimension, and rank."
        }
      ]
    },
    {
      title: "Part III. Direction, Approximation, and Decomposition",
      summary:
        "Study invariant directions, approximation, and the decompositions that organize complex linear behavior.",
      items: [
        {
          text: "Chapter 9. Orthogonality and Least Squares",
          link: "/chapters/09-orthogonality-and-least-squares",
          file: "chapters/09-orthogonality-and-least-squares.md",
          description:
            "Dot products, projections, orthonormal bases, and fitting imperfect data."
        },
        {
          text: "Chapter 10. Eigenvalues and Eigenvectors",
          link: "/chapters/10-eigenvalues-and-eigenvectors",
          file: "chapters/10-eigenvalues-and-eigenvectors.md",
          description:
            "Invariant directions, scaling factors, and why some directions matter more than others."
        },
        {
          text: "Chapter 11. Diagonalization and Dynamics",
          link: "/chapters/11-diagonalization-and-dynamics",
          file: "chapters/11-diagonalization-and-dynamics.md",
          description:
            "Repeated matrix action, powers of matrices, and discrete-time systems."
        },
        {
          text: "Chapter 12. Symmetric Matrices and Quadratic Forms",
          link: "/chapters/12-symmetric-matrices-and-quadratic-forms",
          file: "chapters/12-symmetric-matrices-and-quadratic-forms.md",
          description:
            "Energy, curvature, ellipses, principal axes, and why symmetry simplifies everything."
        },
        {
          text: "Chapter 13. Singular Value Decomposition",
          link: "/chapters/13-singular-value-decomposition",
          file: "chapters/13-singular-value-decomposition.md",
          description:
            "Rotate, stretch, rotate again: the geometry and power of SVD."
        }
      ]
    },
    {
      title: "Part IV. Applications and Computation",
      summary:
        "Apply matrix thinking to networks, data, continuous systems, and real computational constraints.",
      items: [
        {
          text: "Chapter 14. Matrices in Networks and Markov Chains",
          link: "/chapters/14-matrices-in-networks-and-markov-chains",
          file: "chapters/14-matrices-in-networks-and-markov-chains.md",
          description:
            "Graphs, transitions, walks, steady states, and long-run behavior."
        },
        {
          text: "Chapter 15. Matrices in Data, Images, and Machine Learning",
          link: "/chapters/15-matrices-in-data-images-and-ml",
          file: "chapters/15-matrices-in-data-images-and-ml.md",
          description:
            "Datasets, features, image grids, embeddings, covariance intuition, and practical modeling ideas."
        },
        {
          text: "Chapter 16. Differential Equations and Continuous Systems",
          link: "/chapters/16-differential-equations-and-continuous-systems",
          file: "chapters/16-differential-equations-and-continuous-systems.md",
          description:
            "Coupled systems, matrix exponentials, and continuous-time dynamics."
        },
        {
          text: "Chapter 17. Numerical Linear Algebra",
          link: "/chapters/17-numerical-linear-algebra",
          file: "chapters/17-numerical-linear-algebra.md",
          description:
            "Floating point arithmetic, conditioning, stability, and the computational reality of matrix problems."
        },
        {
          text: "Chapter 18. Cheat Sheet and Next Steps",
          link: "/chapters/18-cheat-sheet-and-next-steps",
          file: "chapters/18-cheat-sheet-and-next-steps.md",
          description:
            "A synthesis chapter with concept links, pitfalls, and directions for further study."
        }
      ]
    }
  ],
  appendices: [
    {
      text: "Appendix A. Guided Problems and Mini-Solutions",
      link: "/chapters/appendix-a-guided-problems-and-mini-solutions",
      file: "chapters/appendix-a-guided-problems-and-mini-solutions.md",
      description:
        "Worked practice that shows how to attack representative matrix problems step by step."
    },
    {
      text: "Appendix B. Visual Glossary and Symbol Guide",
      link: "/chapters/appendix-b-visual-glossary-and-symbol-guide",
      file: "chapters/appendix-b-visual-glossary-and-symbol-guide.md",
      description:
        "A notation guide and translation map between algebraic, geometric, and applied viewpoints."
    }
  ]
};

export const allEntries = book.parts.flatMap((part) => part.items).concat(book.appendices);

export function buildSidebar() {
  return [
    {
      text: "Start Here",
      items: [
        { text: "Home", link: "/" },
        { text: "Project README", link: "/README" }
      ]
    },
    ...book.parts.map((part) => ({
      text: part.title,
      items: part.items.map(({ text, link }) => ({ text, link }))
    })),
    {
      text: "Appendices",
      items: book.appendices.map(({ text, link }) => ({ text, link }))
    }
  ];
}
