"""
Reusable visualization functions for the DSA Math Intuition Lab.

These eliminate code duplication across notebooks and model good
software engineering for the learner.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot_growth_comparison(n_max=50, growth_rates=None, log_scale=False, ax=None):
    """Plot multiple growth rate curves on the same axes.
    
    Parameters
    ----------
    n_max : int
        Maximum input size to plot.
    growth_rates : dict or None
        Mapping of label → function(n). If None, uses standard rates.
    log_scale : bool
        Whether to use log scale on y-axis.
    ax : matplotlib.axes.Axes or None
        Axes to plot on. Creates new figure if None.
    
    Returns
    -------
    ax : matplotlib.axes.Axes
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(9, 5))
    
    n = np.linspace(1, n_max, 500)
    
    if growth_rates is None:
        growth_rates = {
            'O(1)':       lambda n: np.ones_like(n),
            'O(log n)':   lambda n: np.log2(n),
            'O(n)':       lambda n: n,
            'O(n log n)': lambda n: n * np.log2(n),
            'O(n²)':      lambda n: n**2,
        }
    
    colors = ['#10b981', '#06b6d4', '#6366f1', '#8b5cf6', '#f43f5e', '#ef4444',
              '#f97316', '#eab308', '#14b8a6']
    
    for i, (name, func) in enumerate(growth_rates.items()):
        color = colors[i % len(colors)]
        ax.plot(n, func(n), label=name, color=color, linewidth=2)
    
    if log_scale:
        ax.set_yscale('log')
    
    ax.set_xlabel('n (input size)', fontsize=12)
    ax.set_ylabel('Operations', fontsize=12)
    ax.set_title(f'Growth Rates (n up to {n_max})', fontsize=13, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    
    return ax


def plot_transformation(M, title='', ax=None):
    """Visualize what a 2x2 matrix does to the unit square and basis vectors.
    
    Parameters
    ----------
    M : np.ndarray
        2×2 transformation matrix.
    title : str
        Plot title.
    ax : matplotlib.axes.Axes or None
        Axes to plot on. Creates new figure if None.
    
    Returns
    -------
    ax : matplotlib.axes.Axes
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(6, 6))
    
    # Unit square corners
    square = np.array([[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]).T
    transformed = M @ square
    
    # Draw original (faded)
    ax.fill(square[0], square[1], alpha=0.1, color='gray')
    ax.plot(square[0], square[1], 'k--', alpha=0.3, linewidth=1)
    
    # Draw transformed
    ax.fill(transformed[0], transformed[1], alpha=0.25, color='#6366f1')
    ax.plot(transformed[0], transformed[1], color='#6366f1', linewidth=2)
    
    # Basis vectors: original
    ax.annotate('', xy=(1, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5, alpha=0.4))
    ax.annotate('', xy=(0, 1), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5, alpha=0.4))
    
    # Basis vectors: transformed
    e1 = M @ np.array([1, 0])
    e2 = M @ np.array([0, 1])
    ax.annotate('', xy=e1, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#f43f5e', lw=2.5))
    ax.annotate('', xy=e2, xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#10b981', lw=2.5))
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.set_title(title, fontsize=12, fontweight='bold')
    return ax


def draw_tree(tree, ax, x=0, y=0, span=1, parent_pos=None):
    """Recursively draw a tree structure on matplotlib axes.
    
    Parameters
    ----------
    tree : dict
        Tree node with keys: 'label', 'depth', 'is_leaf', 'children'.
    ax : matplotlib.axes.Axes
        Axes to draw on.
    x, y : float
        Position of this node.
    span : float
        Horizontal span for children.
    parent_pos : tuple or None
        (x, y) of parent node for drawing connecting line.
    """
    color = '#10b981' if tree['is_leaf'] else '#6366f1'
    size = 8 if tree['is_leaf'] else 6
    
    ax.plot(x, y, 'o', color=color, markersize=size, zorder=3)
    
    if parent_pos is not None:
        ax.plot([parent_pos[0], x], [parent_pos[1], y], '-', color='#94a3b8',
                linewidth=0.8, zorder=1)
    
    if tree['is_leaf']:
        ax.text(x, y - 0.3, tree['label'], ha='center', fontsize=6, color='#10b981')
    
    n_children = len(tree.get('children', []))
    if n_children > 0:
        child_span = span / max(n_children, 1)
        start_x = x - span / 2 + child_span / 2
        for i, child_tree in enumerate(tree['children']):
            child_x = start_x + i * child_span
            draw_tree(child_tree, ax, child_x, y - 1, child_span * 0.9, (x, y))


def style_axis(ax, title='', xlabel='', ylabel='', grid=True):
    """Apply consistent styling to an axis."""
    if title:
        ax.set_title(title, fontsize=13, fontweight='bold')
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=12)
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=12)
    if grid:
        ax.grid(True, alpha=0.3)
    return ax
