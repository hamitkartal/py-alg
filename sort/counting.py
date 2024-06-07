from typing import List

def counting_sort(arr: List[int]) -> List[int]:
    """Counting Sort Algorithm"""
    
    # Return the array if has 0 or 1 elements
    if len(arr) <= 1:
        return arr
    
    # Set-up process of normalisation
    min_ = min(arr)
    max_ = max(arr)
    range_of_arr = max_ - min_ + 1
    
    # Initialize a 0-array length of range_of_arr
    count_arr = [0] * range_of_arr
    
    # Store the count of each element in the array
    for elem in arr:
        count_arr[elem - min_] += 1
    
    # Cumulative summation of array
    for indx in range(1, len(count_arr)):
        count_arr[indx] += count_arr[indx-1]
    
    # Initiliaze a 0-array length of input array
    output_arr = [0] * len(arr)

    # Put the elements in the correct position
    for r_index in range(len(arr)-1 , -1, -1):
        current_elem = arr[r_index]
        position = count_arr[current_elem - min_] - 1
        output_arr[position] = current_elem
        count_arr[current_elem - min_] -= 1
    
    # Return the output
    return output_arr

