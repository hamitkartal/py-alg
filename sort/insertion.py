from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Selection Sort Algorithm
    """
    """
    Return the array itself if the number of
    elements in the array are smaller than 1
    """
    N = len(arr)
    if N <= 1:
        return arr

    """
    Then we traverse the array 1-by-1
    """
    for index in range(1, N):
        """
        Store the key in each iteration
        """
        num = arr[index]

        """
        Assign the traveler point
        """
        ptr = index - 1
        """
        Shifting each element one to right
        position, until we hit the end or
        an element smaller (or equal) to
        the key number
        """
        while ptr >= 0 and arr[ptr] > num:
            arr[ptr+1] = arr[ptr]
            ptr -= 1
        
        """
        Then insert the key element to the
        correct position
        """
        arr[ptr+1] = num
    return arr
