# 🎲 Randomness and Expectation

> *Randomness isn't chaos — it's a tool. Algorithms use it to turn worst cases into average cases.*

---

## Why This Matters

Deterministic algorithms can be cornered. A carefully crafted input can force QuickSort into O(n²). But add randomness — pick a random pivot — and the adversary loses power.

Key ideas for DSA:
- **Expected value** tells you what happens *on average*, not in one run
- **Monte Carlo methods** give approximate answers fast — often faster than exact algorithms
- **Randomized algorithms** (QuickSort, hashing, skip lists) trade worst-case guarantees for excellent average-case performance

---

## Notebooks

| # | Notebook | Focus |
|---|---------|-------|
| 1 | `01_randomized_behavior.ipynb` | QuickSort analysis, Monte Carlo π, convergence |
| 2 | `02_exercises.ipynb` | 🟢🟡🔴 Self-test with auto-checked answers |

---

## Key Insight

Randomized QuickSort doesn't guarantee O(n log n) for a *single* run. It guarantees that the *expected* runtime — averaged over the randomness — is O(n log n) for *any* input.

The adversary can choose the worst input. But they can't choose your coin flips.
