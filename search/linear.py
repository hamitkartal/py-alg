from typing import List


def linear_search(arr: List[int], target: int) -> int:
    """
    Linear Search Algorithm
    
    If target exists in the arr,
        Returns the index
    Otherwise,
        Returns -1
    
    1) Array does not need to be sorted
    2) Algorithm returns the index of the
        first occurence.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1