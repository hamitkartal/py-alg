from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    """
    Selection Sort Algorithm
    """

    # Return the array itself if
    # number of elements are smaller than 1
    N = len(arr)
    if N <= 1:
        return arr

    # In each iteration, we select the right
    # position for the next smallest element
    for i in range(N):

        # This piece basically finds the minimum
        min_index = i
        for index in range(i, N):
            if arr[index] <= arr[min_index]:
                min_index = index
        
        # After we find the minimum in the interval,
        # we swap it with the position we kept for
        # the smallest number
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
