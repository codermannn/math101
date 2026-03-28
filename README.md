# 🧠 Math101 — DSA Math Intuition Lab

> *"What I cannot create, I do not understand."* — Richard Feynman

A self-learning laboratory built completely from first principles. Instead of burying you in academic definitions, this repository assumes that **tinkering with broken code** produces mathematics intuitively. 

---

## 🚀 Quick Start

1. Install dependencies with `uv sync`
2. Launch Jupyter Lab with `uv run jupyter lab`
3. **Open `00_START_HERE.ipynb`**. Do not manually click through folders. Let the Control Panel hold your hand.

You'll notice you don't need `sys.path` hacks. `src/math101` automatically installs itself as a local utility library during `uv sync`.

---

## 📚 Concept Dependency Graph & Reading Order

Follow this exact structure. Do not skip ahead — mathematics is a dependency graph, not a list.

```text
math101/
├── 00_START_HERE.ipynb                           → MUST OPEN THIS FIRST! It acts as your Master Control Panel.
│
├── 01-seeing-with-code/
│   ╰── 01_visualization_toolbox.ipynb            → Build a visceral connection between Python arrays and visual graphs.
│
├── 02-how-things-scale/                          « START CORE CONCEPTS HERE »
│   ├── 01_growth_rates_and_big_o.ipynb           → Use sliders to feel exponential vanishing terms.
│   ╰── 02_recurrences_and_master_theorem.ipynb   → Look at exploding recurrence trees geometrically.
│
├── 03c-when-choices-explode/                     « COMBINATORICS TRACK »
│   ├── 01_recursion_trees_and_counting.ipynb     → Why a simple maze search takes a billion steps.
│   ╰── 02_dynamic_programming.ipynb              → Fixing overlapping branches via memoized intuition.
│
├── 03a-transforming-space/                       « GEOMETRY TRACK »
│   ├── 01_vectors_and_matrices.ipynb             → Watch 2D arrays transform space dynamically.
│   ╰── 02_graphs_encoded_as_matrices.ipynb       → Adjacency matrices as transformation pipelines.
│
├── 03b-taming-uncertainty/                       « PROBABILITY TRACK »
│   ╰── 01_randomized_behavior.ipynb              → Force algorithms to gamble and observe expected outcomes.
│
╰── 04-putting-it-together/                       « SYNTHESIS »
    ╰── 01_complexity_of_randomized_algorithms.ipynb → Master the intersection of graph limits and randomness.
```

*(Note: The separate `exercises.ipynb` notebooks were explicitly merged into the core notebooks under the **Break-It Lab** sections. The separation between theory and practice is an academic illusion.)*

---

## 🧬 The Arc of Every Concept
Do not skip around within a notebook! Each one operates under a strict psychological sequence:

1. **The Hook**: A baffling question to make you curious.
2. **The Playground**: Interact with the sliders. Break the system before seeing the math.
3. **The Pattern**: "What did you notice?"
4. **⚠️ Common Wrong Intuition**: Explicitly debunking the worst assumption people make.
5. **The Explanation (ADEPT)**: Analogy → Diagram → Example → Plain English → Math.
6. **The Proof**: Geometric logic over raw algebra.
7. **🔬 Break-It Lab**: Tinkering and pushing the inputs to destruction to find limits.
8. **The Feynman Technique**: You forcing yourself to explain it back.
9. **Review**: Pre-made flashcards ready to dump into your Anki.

---

## 🔧 AI Copilot Guide
Using Claude or ChatGPT? Feed it `LLM_PROMPT.md` **before** asking for help. It enforces our rigorous visual pedagogy mapping and bans textbook-style exposition.

---

## 🧠 Curated Deep-Dive Resources

| Domain | Best free interactive resource | Best book for depth | Best video for intuition |
|--------|-------------------------------|---------------------|--------------------------|
| **Linear Algebra** | [Immersive Math](http://immersivemath.com/ila/index.html) | *Linear Algebra Done Right* by Sheldon Axler | 3Blue1Brown: *Essence of Linear Algebra* |
| **Growth Rates / DSA** | [VisuAlgo.net](https://visualgo.net/) | *Grokking Algorithms* by Bhargava | BetterExplained: *Sorting algorithms intuition* |
| **Probability** | [Seeing Theory](https://seeingtheory.brown.edu/) | *The Art of Probability* by Richard Hamming | 3Blue1Brown: *Binomial distributions* |
