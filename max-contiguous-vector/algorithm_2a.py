"""This algorithm takes O(n**2)"""

from typing import List


def main(vector: List[float]) -> float:
    length = len(vector)

    max_so_far = 0
    for i in range(length):
        total = 0
        for j in range(i, length):
            total += vector[j]
            max_so_far = max(max_so_far, total)
    return max_so_far


if __name__ == "__main__":
    test_vector = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    assert main(test_vector) == 187
