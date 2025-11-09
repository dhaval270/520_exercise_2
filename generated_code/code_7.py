from __future__ import annotations

from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Return ``True`` if any two distinct elements in *numbers* are closer to each other
    than *threshold*.

    The function works for any numeric type that supports subtraction and
    absolute value (``float`` and ``int`` are the usual cases).  It is
    intentionally tolerant of an empty list or a list with a single element –
    in those cases the answer is always ``False`` because there is no pair to
    compare.

    Parameters
    ----------
    numbers : List[float]
        The list of numbers to examine.
    threshold : float
        The distance below which two numbers are considered “close”.
        If *threshold* is less than or equal to zero the function will
        immediately return ``False`` because a non‑negative distance can
        never be smaller than a non‑positive threshold.

    Returns
    -------
    bool
        ``True`` if at least one pair of numbers is closer than *threshold*,
        otherwise ``False``.

    Examples
    --------
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    >>> has_close_elements([], 1.0)
    False
    >>> has_close_elements([5], 0.1)
    False
    """
    # Quick exit for trivial cases
    if threshold <= 0:
        return False
    n = len(numbers)
    if n < 2:
        return False

    # Sorting allows us to check only adjacent pairs – the smallest
    # possible distance in a sorted list is always between neighbours.
    sorted_numbers = sorted(numbers)
    for i in range(n - 1):
        if abs(sorted_numbers[i + 1] - sorted_numbers[i]) < threshold:
            return True
    return False


# --------------------------------------------------------------------------- #
# The following block is only executed when the module is run as a script.
# It demonstrates the function and runs the doctest examples.
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    import doctest
    doctest.testmod()