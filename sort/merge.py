from typing import List

def intertwine(arr1: List[int], arr2: List[int]) -> List[int]:
    ptr_1 = 0
    ptr_2 = 0
    intertwined = []
    while ptr_1 < len(arr1) and ptr_2 < len(arr2):
        if arr1[ptr_1] > arr2[ptr_2]:
            intertwined.append(arr2[ptr_2])
            ptr_2 += 1
        else:
            intertwined.append(arr1[ptr_1])
            ptr_1 += 1
    
    if ptr_1 == len(arr1):
        arr, ptr = arr2, ptr_2
    else:
        arr, ptr = arr1, ptr_1
    
    while ptr < len(arr):
        intertwined.append(arr[ptr])
        ptr += 1
    
    return intertwined

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) in (0, 1):
        return arr
    mid_index = len(arr) // 2
    return intertwine(merge_sort(arr[0:mid_index]), merge_sort(arr[mid_index:]))
