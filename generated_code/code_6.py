from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.

    Args:
        numbers (List[float]): A list of floating point numbers.
        threshold (float): The minimum distance between two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.
    """

    # Handle edge case: empty list
    if len(numbers) < 2:
        return False

    # Handle edge case: threshold value of zero or less
    if threshold <= 0:
        raise ValueError("Threshold must be greater than zero")

    # Sort the list of numbers in ascending order
    numbers.sort()

    # Iterate through the sorted list, comparing each number with its next number
    for i in range(len(numbers) - 1):
        # If the difference between any two adjacent numbers is less than or equal to the threshold, return True
        if numbers[i + 1] - numbers[i] <= threshold:
            return True

    # If no such pair is found after iterating through the entire list, return False
    return False

# Example usage:
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True