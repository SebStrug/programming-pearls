"""Divide and conquer recipe: to solve a problem of size n, recursively
solve two subproblems of size ~n/2, and combine their solutions to yield
a solution to the complete problem.

This algorithm is O(n*logn)
"""
from typing import List


def main(vector: List[float], left_index: int, right_index: int) -> float:
    """Find the largest contiguous subvector in a given vector

    Args:
        vector: input to find largest contiguous subvector for
        left_index: maximum left index of the input vector
        right_index: maximum right index of the input vector
    """
    # Handle base recursive cases
    # 0 elements
    if left_index > right_index:
        return 0
    # 1 element
    if left_index == right_index:
        return max(0, vector[left_index])

    mid_index = (left_index + right_index) // 2
    # find max crossing to the left
    l_max, total = 0, 0
    for i in reversed(range(1, mid_index + 1)):
        total += vector[i]
        l_max = max(l_max, total)
    # find max crossing to the right
    r_max, total = 0, 0
    for i in range(mid_index, right_index - 1):
        total += vector[i]
        r_max = max(r_max, total)

    return max(l_max + r_max, main(vector, left_index, mid_index), main(vector, mid_index + 1, right_index))


if __name__ == "__main__":
    test_vector = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    assert main(test_vector, 0, len(test_vector) - 1) == 187
