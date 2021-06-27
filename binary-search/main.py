from typing import List

def binary_search(array: List[int], val: int) -> int:
    """Run a binary search to find the index of a value in a sorted array
    
    Args:
        array: Sorted list of integers to search over.
        val: Integer value to search for.

    Returns:
        Index of value in array. Raise ValueError if no such value in array.
    """
    if len(array) == 0:
        raise ValueError

    half_length = len(array) // 2
    half_val = array[half_length]
    if half_val == val:
        return half_length
    # Catch a non-existent element
    if len(array) == 1 and half_val != val:
        raise ValueError

    if half_val > val:
        return binary_search(array[:half_length], val)
    if half_val < val:
        return half_length + binary_search(array[half_length:], val)
