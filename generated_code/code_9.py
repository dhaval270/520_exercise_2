from __future__ import annotations
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Return True if any two distinct numbers in *numbers* are closer to each other
    than *threshold*.

    The algorithm sorts the list once (O(n log n)) and then scans the sorted
    sequence, comparing only adjacent pairs.  Adjacent pairs are the only ones
    that can be the closest after sorting, so this is optimal for a general
    list of floats.

    Parameters
    ----------
    numbers : List[float]
        The list of numbers to examine.
    threshold : float
        The distance threshold.  If it is negative, the function returns
        False because no distance can be negative.

    Returns
    -------
    bool
        True if there exist i < j such that |numbers[i] - numbers[j]| < threshold,
        otherwise False.

    Examples
    --------
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    >>> has_close_elements([], 1.0)
    False
    >>> has_close_elements([5.0], 0.1)
    False
    >>> has_close_elements([1.0, 1.0], 0.0)
    False
    >>> has_close_elements([1.0, 1.0], 0.1)
    True
    """
    # No pair can exist if we have fewer than 2 elements or a non‑positive threshold.
    if len(numbers) < 2 or threshold <= 0:
        return False

    # Sort once; adjacent elements in the sorted order are the only candidates
    # that can be the closest pair.
    sorted_nums = sorted(numbers)

    # Scan adjacent pairs.
    for a, b in zip(sorted_nums, sorted_nums[1:]):
        if abs(b - a) < threshold:
            return True

    return False