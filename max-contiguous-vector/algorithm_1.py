"""This algorithm takes O(n**3)"""

from typing import List


def main(vector: List[float]) -> float:
    length = len(vector)

    max_so_far = 0
    for i in range(length):
        for j in range(i, length):
            total = 0
            for k in range(i, j+1):
                total += vector[k]
            max_so_far = max(max_so_far, total)
    return max_so_far


if __name__ == "__main__":
    test_vector = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    assert main(test_vector) == 187
