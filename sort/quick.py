from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort Algorithm

    This is the end-point of this module
    When a user wants to apply quick sort alg
        on an array, s/he wouldn't care about the
        low/high parameters, s/he would just want
        to apply the algorithm.
    Therefore, I put an intermediate (quick_sort)
        function and explicitly indicate the low/high
        parameters.
    """
    return intermediate_quick_sort(arr, 0, len(arr)-1)

def partition(arr: List[int], low: int, high: int) -> int:
    
    # We set the pivot as the last element
    pivot = arr[high]
    
    # Set the slower pointer as (low-1)
    # since it should keep pointing to the
    # right-most smaller element
    # and swapping operation between the pivot
    # and the left-most bigger element will be
    # simpler
    i = low - 1

    # Traverse the entire array until we find
    # an element smaller than pivot
    # We keep i pointing to the smallest right-most
    # element by swapping arr[i] and arr[j]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Then we swap the pivot and the left-most
    # larger element
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def intermediate_quick_sort(arr: List[int], low: int, high: int) -> List[int]:
    """
    Until low < high, we perform partition on the array we have
    and by using the partitioned index, we keep applying intermediate_
    quick_sort function recursively.
    """
    if low < high:
        partition_index = partition(arr, low, high)
        intermediate_quick_sort(arr, low, partition_index-1)
        intermediate_quick_sort(arr, partition_index+1, high)
    return arr

if __name__ == '__main__':
    arr = [4, 1, 7, 3, 8, 2, 5, 6]
    print(quick_sort(arr))
    # print(partition(arr, 0, len(arr)-1))
    
