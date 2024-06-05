from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """
    Binary search algorithm
    If target exists in the array,
        Returns the index of the target
    Otherwise,
        Returns -1
    1) Algortihm ASSUMES array is sorted in ascending
    2) Algorithm returns the first occurence
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            if mid == 0 or arr[mid-1] < target:
                return mid
            right = mid - 1

        if arr[mid] < target:
            left = mid+1

        else: # arr[mid] > target
            right = mid - 1
    return -1
