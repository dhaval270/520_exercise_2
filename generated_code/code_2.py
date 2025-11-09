from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in the given list of numbers, are any two numbers closer to each other than the given threshold.
    
    Args:
    numbers (List[float]): A list of floating-point numbers.
    threshold (float): The minimum distance required between any two numbers.
    
    Returns:
    bool: True if any two numbers are closer than the threshold, False otherwise.
    """
    
    # First, sort the list of numbers
    numbers.sort()
    
    # Iterate over the sorted list to compare adjacent elements
    for i in range(len(numbers) - 1):
        # Calculate the difference between the current element and the next one
        difference = abs(numbers[i] - numbers[i + 1])
        
        # If the difference is less than or equal to the threshold, return True
        if difference <= threshold:
            return True
    
    # If no pair of numbers is closer than the threshold, return False
    return False

# Example usage
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # False
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # True