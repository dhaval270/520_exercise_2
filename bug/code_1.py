from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Return ``True`` if any two numbers in *numbers* are closer to each other
    than *threshold*.

    The function works in O(n log n) time by sorting the list first and then
    checking only adjacent elements – after sorting, the smallest distance
    between any two numbers must be between two neighbours.

    Parameters
    ----------
    numbers : List[float]
        The list of numbers to inspect.
    threshold : float
        The distance threshold.  If *threshold* is non‑positive, the
        function will always return ``False`` because the absolute
        difference between two real numbers is never negative.

    Returns
    -------
    bool
        ``True`` if a pair of numbers is closer than *threshold*,
        otherwise ``False``.

    Examples
    --------
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) < 2 or threshold <= 0:
        return False

    # Sort once; then only adjacent pairs can be the closest.
    sorted_numbers = sorted(numbers)
    for i in range(1, len(sorted_numbers)):
        if abs(sorted_numbers[i] - sorted_numbers[i - 1]) < threshold:
            return True
    return False