"""This algorithm is O(n)"""
from typing import List

def main(vector: List[float]) -> float:
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, len(vector)):
        max_ending_here = max(max_ending_here + vector[i], 0)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

if __name__ == "__main__":
    test_vector = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    assert main(test_vector) == 187
