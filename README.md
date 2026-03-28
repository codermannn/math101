# 🧠 Math101 — DSA Math Intuition Lab

> *"What I cannot create, I do not understand."* — Richard Feynman

A repository completely redesigned to teach the **mathematical intuition** behind data structures and algorithms. 

This repository fundamentally rejects the academic instinct of: `Definition → Theorem → Proof → Example`.  
Instead, every single notebook enforces the opposite: **`Question → Play → Pattern → Explanation → Formalism`**.

---

## 🚀 Quick Start & How to Move Through the Repo

```bash
# Install dependencies
uv sync

# Launch Jupyter (Ensure your widgets are working!)
uv run jupyter lab
```

### The `src/math101/` Arsenal: Keeping Notebooks Clean
Because you ran `uv sync`, the `src/math101` folder is automatically installed as a local package. 
**Never clutter your notebooks with 50-line `matplotlib` or algorithm setups!**
If an interactive visualization takes a lot of helper code, write it inside `src/math101/viz.py` and simply import it into your notebook like a native library:

```python
# No ugly sys.path hacks required! Just import directly:
from math101.viz import plot_interactive_matrix

plot_interactive_matrix() 
```

### The Arc of Every Concept
Do not skip around within a notebook. Follow the psychological arc meticulously designed into every `.ipynb` file:

1. **The Hook**: You will be confronted with an approachable but surprising question.
2. **The Playground**: **STOP READING.** Play with the `ipywidgets` sliders. Push them to the extremes. *Feel* the data before any math is introduced.
3. **The Pattern**: What did you notice? This is your *Aha!* moment.
4. **⚠️ Common Wrong Intuition**: We explicitly state the way most people get this wrong. Correcting bad assumptions builds durable understanding.
5. **The Explanation (ADEPT)**: Analogy → Diagram → Example → Plain English → Technical Definition.
6. **The Proof**: Geometric and visual proofs over symbolic algebra.
7. **🔬 Break-It Lab**: We wrote code that works. Your job is to break it, find out why, and fix it. There are no "isolated exercises." Tinkering *is* doing.
8. **The Feynman Technique**: You must explain it in the empty cell provided without jargon.
9. **Review**: Extract these Q/A pairs to your Anki.

---

## 📚 Concept Dependency Graph

Move through the repository structurally, not chronologically.

```text
math101/
├── 00-are-you-ready/         ← Diagnostic hooks.
├── 01-seeing-with-code/      ← Learn your visualization tools (matplotlib, plotly).
├── 02-how-things-scale/      ← Start Here. Big-O, vanishing terms, recurrences.
│   └── ↳ 03c-when-choices-explode/  ← Depends on scaling. Permutations, Recursion Trees, DP.
├── 03a-transforming-space/   ← Independent Track: Matrices, linear transformations, geometric intuition.
└── 03b-taming-uncertainty/   ← Independent Track: Randomness, Monte Carlo, Expected values.
    └── ↳ 04-putting-it-together/    ← Synthesis. Mixing algorithms with randomness and space.

Global Tools:
├── animations/               ← Standalone Manim code for cinematic visualisations.
├── scratch/                  ← Free exploration and messy ideas. Never commit polished work here.
├── INSIGHTS.md               ← Your ongoing log of "Aha!" and "Huh?" moments.
├── REVIEW.md                 ← Central aggregator for spaced repetition flashcards.
└── math101_template.ipynb    ← Start here for every new concept. Use it.
```

---

## 🔧 AI Copilot Guide

If you are using an LLM to assist you, **always feed the AI the `LLM_PROMPT.md` file first**. It forces the model to abandon textbook-style lecturing and adhere to our strict pedagogical principles of visually scaffolding math.

---

## 🧠 Curated Deep-Dive Resources

| Domain | Best free interactive resource | Best book for depth | Best video for intuition |
|--------|-------------------------------|---------------------|--------------------------|
| **Linear Algebra** | [Immersive Math](http://immersivemath.com/ila/index.html) (Interactive textbook) | *Linear Algebra Done Right* by Sheldon Axler | 3Blue1Brown: *Essence of Linear Algebra* |
| **Growth Rates / DSA** | [VisuAlgo.net](https://visualgo.net/) | *Grokking Algorithms* by Aditya Bhargava | BetterExplained: *Sorting algorithms intuition* & CS50 |
| **Probability** | [Seeing Theory](https://seeingtheory.brown.edu/) (Brown University) | *The Art of Probability* by Richard Hamming | 3Blue1Brown: *Binomial distributions / Bayes Theorem* |
| **Calculus** *(For bridging)* | [Desmos Calculus Art](https://www.desmos.com/) *(Building derivatives visually)* | *Calculus Made Easy* by Silvanus P. Thompson | 3Blue1Brown: *Essence of Calculus* |

*Built for those who want to play with the machinery of algorithms, not just memorize how they turn on.*