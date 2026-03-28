# 💥 Combinatorics and Explosions

> *Combinatorics is the mathematics of counting. And counting shows you exactly when brute force dies.*

---

## Why This Matters

Every time you write a recursive algorithm, you're implicitly building a **tree of choices**. Each node is a decision, each branch is an option. The total work is the total number of nodes.

Key ideas for DSA:
- **Permutations** (n!) — every ordering of n elements. Grows astronomically fast.
- **Combinations** (C(n,k)) — choosing k items from n. Core of subset problems.
- **Recursion trees** — the actual shape of your computation. Visualizing them reveals the cost.
- **Backtracking** — the art of pruning branches you know will fail.
- **Dynamic programming** — eliminating redundant computation in the recursion tree.

---

## Notebooks

| # | Notebook | Focus |
|---|---------|-------|
| 1 | `01_recursive_tree_growth.ipynb` | Permutation trees, pruning, backtracking |
| 2 | `02_exercises.ipynb` | 🟢🟡🔴 Self-test with auto-checked answers |
| 3 | `03_dynamic_programming.ipynb` | DP as deduplication of the recursion tree |

---

## Key Insight

An algorithm that tries "all possibilities" is building a tree with branching factor × depth = total nodes. Combinatorics gives you the exact price of exhaustive search — and explains why pruning and DP are so powerful.
