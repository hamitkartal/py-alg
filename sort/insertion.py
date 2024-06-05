from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    N = len(arr)
    if N <= 1:
        return arr
    for index in range(1, N):
        num = arr[index]
        ptr = index - 1
        while ptr >= 0 and arr[ptr] > num:
            arr[ptr+1] = arr[ptr]
            ptr -= 1
        arr[ptr+1] = num
    return arr
