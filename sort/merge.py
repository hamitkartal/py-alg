from typing import List

def intertwine(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Function takes two array of integers
    """

    """Traverses the arrays by pointers"""
    ptr_1 = 0
    ptr_2 = 0
    intertwined = []

    """
    Until one array is consumed, the integers
    pointed by the corresponding pointers
    are compared, smaller one is appended
    at the end of the new array
    """
    while ptr_1 < len(arr1) and ptr_2 < len(arr2):
        if arr1[ptr_1] > arr2[ptr_2]:
            intertwined.append(arr2[ptr_2])
            ptr_2 += 1
        else:
            intertwined.append(arr1[ptr_1])
            ptr_1 += 1
    
    """
    Detects wich array is consumed
    Assigns the unconsumed array to arr&ptr
    """
    if ptr_1 == len(arr1):
        arr, ptr = arr2, ptr_2
    else:
        arr, ptr = arr1, ptr_1
    
    """
    Until ptr goes out of bounds
    Appends the remained elements of unconsumed
    array at the end of the new array
    """
    while ptr < len(arr):
        intertwined.append(arr[ptr])
        ptr += 1
    
    """
    Returns the new array
    """    
    return intertwined

def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort Algorithm
    Function takes an array
    If array has 0 or 1 element,
        Returns the array itself
    Otherwise,
        Returns the intertwined array of merge-sorted
        version of both each half.
    """
    if len(arr) in (0, 1):
        return arr
    mid_index = len(arr) // 2
    return intertwine(merge_sort(arr[0:mid_index]), merge_sort(arr[mid_index:]))
