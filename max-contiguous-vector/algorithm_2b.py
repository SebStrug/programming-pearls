"""This algorithm is O(n**2)"""

from typing import List


def main(vector: List[float]) -> float:
    """Access a data structure before the outer look in
    Algorithm 2 is executed. The ith element of a cumulative array
    contains the cumulative sum of the values of x[0..i] so the
    sum of the values x[i..j] from the array
    """
    length = len(vector)

    cum_array = [0] * length
    for i in range(length):
        cum_array[i] = cum_array[i - 1] + vector[i]

    max_so_far = 0
    for i in range(length):
        for j in range(1, length):
            total = cum_array[j] - cum_array[i - 1]
            max_so_far = max(max_so_far, total)
    return max_so_far


if __name__ == "__main__":
    test_vector = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    assert main(test_vector) == 187
