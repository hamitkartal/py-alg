from typing import List
import sys


def kadane(arr: List[int]) -> float:
    max_ = float('-inf')
    for elem in arr:
        if max_ + elem > max_:
            max_ += elem
    return max_


print(kadane([1, 2, 3]))
