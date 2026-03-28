"""
Shared algorithm implementations for the DSA Math Intuition Lab.

Each algorithm is instrumented to count operations, measure time,
or expose internal state — for learning, not production.
"""

import time
import numpy as np


def quicksort_count(arr, random_pivot=True):
    """QuickSort that counts comparisons.
    
    Parameters
    ----------
    arr : list
        Array to sort.
    random_pivot : bool
        If True, pick random pivot. If False, pick first element.
    
    Returns
    -------
    comparisons : int
        Total number of comparisons made.
    """
    comparisons = [0]
    
    def _sort(a):
        if len(a) <= 1:
            return a
        if random_pivot:
            pivot_idx = np.random.randint(len(a))
        else:
            pivot_idx = 0
        pivot = a[pivot_idx]
        left = [x for x in a if x < pivot]
        middle = [x for x in a if x == pivot]
        right = [x for x in a if x > pivot]
        comparisons[0] += len(a) - 1
        return _sort(left) + middle + _sort(right)
    
    _sort(list(arr))
    return comparisons[0]


def binary_search_count(arr, target):
    """Binary search that counts comparisons.
    
    Parameters
    ----------
    arr : list or np.ndarray
        Sorted array to search.
    target : int
        Value to find.
    
    Returns
    -------
    index : int or None
        Index of target, or None if not found.
    comparisons : int
        Number of comparisons made.
    """
    lo, hi = 0, len(arr) - 1
    comparisons = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return None, comparisons


def measure_time(func, n_values, repeats=3):
    """Measure wall-clock time for a function across input sizes.
    
    Parameters
    ----------
    func : callable
        Function that takes a single integer argument n.
    n_values : array-like
        Input sizes to test.
    repeats : int
        Number of repetitions for averaging.
    
    Returns
    -------
    times : np.ndarray
        Average time in seconds for each input size.
    """
    times = []
    for n in n_values:
        trial_times = []
        for _ in range(repeats):
            start = time.perf_counter()
            func(n)
            elapsed = time.perf_counter() - start
            trial_times.append(elapsed)
        times.append(np.median(trial_times))
    return np.array(times)


def count_nodes_full(n):
    """Count total nodes in the full permutation tree of n elements."""
    count = [0]
    def generate(remaining):
        count[0] += 1
        for i in range(len(remaining)):
            generate(remaining[:i] + remaining[i+1:])
    generate(list(range(n)))
    return count[0]


def count_nodes_pruned(n, constraint):
    """Count nodes in a pruned permutation tree.
    
    Parameters
    ----------
    n : int
        Number of elements.
    constraint : callable
        Function that takes a partial permutation (list) and returns
        False if the branch should be pruned.
    """
    count = [0]
    def generate(current, remaining):
        count[0] += 1
        if not constraint(current):
            return
        for i in range(len(remaining)):
            generate(current + [remaining[i]], remaining[:i] + remaining[i+1:])
    generate([], list(range(n)))
    return count[0]


def merge_sort_count(arr):
    """Merge sort that counts comparisons.
    
    Returns
    -------
    sorted_arr : list
        Sorted array.
    comparisons : int
        Total comparisons made.
    """
    comparisons = [0]
    
    def _sort(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = _sort(a[:mid])
        right = _sort(a[mid:])
        return _merge(left, right)
    
    def _merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    sorted_arr = _sort(list(arr))
    return sorted_arr, comparisons[0]


def insertion_sort_count(arr):
    """Insertion sort that counts comparisons."""
    comparisons = 0
    a = list(arr)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    return a, comparisons
