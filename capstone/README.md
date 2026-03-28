# 🏗️ Capstone Project: Algorithm Benchmarking Suite

> *Synthesize everything you've learned into one meaningful project.*

---

## The Challenge

Build a **sorting algorithm benchmarking suite** that:

1. **Implements** at least 4 sorting algorithms (InsertionSort, MergeSort, QuickSort, HeapSort)
2. **Measures** comparisons and wall-clock time across different input sizes
3. **Visualizes** growth curves (Module 1: Growth & Complexity)
4. **Compares** deterministic vs randomized QuickSort (Module 3: Randomness)
5. **Analyzes** the recursion tree structure (Module 4: Combinatorics)
6. **Predicts** performance using recurrence relations and verifies empirically

## Starter Structure

```
CAPSTONE/
├── README.md              ← You're reading this
├── benchmark.py           ← Your benchmarking suite
├── algorithms.py          ← Your sorting implementations
└── analysis.ipynb         ← Your analysis notebook
```

## Requirements

### Phase 1: Implementation
- Implement each algorithm with a comparison counter
- Handle edge cases (empty arrays, single elements, duplicates)
- Write at least 3 unit tests per algorithm

### Phase 2: Measurement
- Test on: sorted, reversed, random, nearly-sorted, few-unique inputs
- Sizes: powers of 2 from 2⁴ to 2¹⁴
- Track: comparisons, swaps, wall-clock time

### Phase 3: Analysis
- Plot empirical vs theoretical growth curves
- For QuickSort: run 100 trials and plot the distribution
- Identify the crossover point where O(n²) algorithms become slower
- Apply the Master Theorem to predict MergeSort and QuickSort complexity

### Phase 4: Report
Create a notebook that tells the story:
1. Which algorithm "wins" and when?
2. When does input type matter and when doesn't it?
3. Does randomized QuickSort match its theoretical expected complexity?
4. At what array size should you switch from InsertionSort to MergeSort?

## Grading Rubric (Self-Assessment)

| Criterion | Points |
|-----------|--------|
| All algorithms implemented correctly | 20 |
| Comprehensive benchmarking across inputs | 20 |
| Clear, well-labeled visualizations | 20 |
| Correct theoretical analysis | 20 |
| Insights and conclusions in report | 20 |

---

*This is where you prove you understand the math — not by repeating formulas, but by building something that uses them.*
