# 📈 Growth and Complexity

> *If your algorithm is slow, it's probably because of growth rates — not bad code.*

---

## Why This Matters

Every algorithm has a **growth function** — how much work it does as the input size increases.

The difference between O(n) and O(2ⁿ) is the difference between "runs in a second" and "outlives the universe."

Understanding growth rates gives you:
- **Instant estimation** of whether an approach is feasible
- **Intuition for trade-offs** between time and space
- **The ability to predict** how algorithms scale before running them

---

## Notebooks

| # | Notebook | Focus |
|---|---------|-------|
| 1 | `01_unified_growth_explorer.ipynb` | All growth rates visualized, asymptotic dominance |
| 2 | `02_exercises.ipynb` | 🟢🟡🔴 Self-test with auto-checked answers |
| 3 | `03_recurrence_relations.ipynb` | Master Theorem, divide & conquer recurrences |

---

## Key Insight

Growth rates aren't about exact numbers. They're about **which term wins when n gets huge**.

$3n^2 + 100n + 999$ behaves like $n^2$ for large $n$. The constant 999, the linear term 100n — they become noise. Only the **dominant term** matters.
