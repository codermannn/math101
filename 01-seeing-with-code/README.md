# 🔧 Visualization Toolbox — Mental Model

> Before you visualize math, understand your tools.

---

## The Core Mental Model

Matplotlib has **two layers**:

```
Figure  (the canvas — the window itself)
  └── Axes  (a single plot area inside the canvas)
        ├── Lines, patches, text  (the visual elements)
        └── Axis  (the x/y rulers with ticks and labels)
```

**Everything is an object.** A plot isn't a picture — it's a tree of Python objects you can inspect, modify, and rebuild.

---

## How to Experiment

### 1. Create, don't memorize
```python
fig, ax = plt.subplots()      # This gives you a Figure and one Axes
ax.plot([1, 2, 3], [1, 4, 9]) # This returns a list of Line2D objects
```

### 2. Inspect everything
```python
line, = ax.plot([1, 2, 3], [1, 4, 9])
type(line)          # matplotlib.lines.Line2D
dir(line)           # every method and property
line.get_color()    # what color is it?
line.get_data()     # what data does it hold?
```

### 3. Modify after creation
```python
line.set_color('red')
line.set_linewidth(3)
line.set_linestyle('--')
fig.canvas.draw()   # refresh to see changes
```

### 4. Explore the hierarchy
```python
fig.get_axes()        # list of all Axes in the Figure
ax.get_children()     # everything inside this Axes
ax.lines              # just the line objects
ax.patches            # just the shape objects
```

---

## How to Modify Behavior Interactively

With `ipywidgets`, you can make any parameter controllable:

```python
from ipywidgets import interact

@interact(slope=(0.1, 5.0, 0.1))
def plot_line(slope=1.0):
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    ax.plot(x, slope * x)
    ax.set_title(f'y = {slope:.1f}x')
    plt.show()
```

The slider becomes your lab instrument. Change the parameter → observe the effect → build intuition.

---

## Key Mindset

| Don't... | Do... |
|----------|-------|
| Memorize function signatures | Inspect objects with `dir()` and `type()` |
| Copy-paste plot code | Build plots piece by piece |
| Treat plots as pictures | Treat plots as object trees |
| Read docs linearly | Experiment, break things, inspect |

---

*The notebook `01_visualization_toolbox.ipynb` puts all of this into practice.*
