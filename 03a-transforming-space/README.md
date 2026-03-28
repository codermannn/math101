# 🔷 Structure and Transformations

> *Algorithms don't just process data — they process **structure**. Matrices encode that structure.*

---

## Why This Matters

When you represent a graph as an adjacency matrix, or apply a page rank, or rotate an image, you're doing **linear algebra**. You're treating mathematical objects as machines that transform input into output.

Key ideas for DSA:
- **Vectors** represent state (position, direction, features)
- **Matrices** represent transformations (rotate, scale, project, connect)
- **Graphs** are matrices — adjacency matrices encode structure directly
- **Transformations compose** — multiply matrices to chain operations

---

## Notebooks

| # | Notebook | Focus |
|---|---------|-------|
| 1 | `01_vectors_and_transformations.ipynb` | 2D transformations, basis vectors, determinant |
| 2 | `02_exercises.ipynb` | 🟢🟡🔴 Self-test with auto-checked answers |
| 3 | `03_graphs_as_matrices.ipynb` | Path counting, PageRank, spectral properties |

---

## Key Insight

A matrix is not a table of numbers. It's a **function**. It takes an input vector and produces an output vector. The numbers in the matrix define *how* the function transforms space.
