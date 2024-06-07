from typing import List

def counting_sort(arr: List[int], exp: int) -> None:
    """ - Digit Based - Counting Sort Algorithm"""

    # Initialize teh counting array between 0 - 9
    count_arr = [0] * 10

    # For each element in the array;
    for elem in arr:
        # Reach to the current digit
        # For example elem = 2 and exp = 100
        # (exp = 100) means that, we are interested
        # with the third LSD. (2 // 100) = 0
        # That means, we treat 2 as 002

        # Second example, elem = 802 and exp = 100
        # (802 // 100) = 8

        # However, if elem = 8802
        # Then (8802 // 100) = 88
        # Now we are interested in the last digit
        position = elem // exp

        # In order to get the value of the last digit,
        # We use '%' operation by 10
        # Then increase the corresponding frequency by 1
        count_arr[position % 10] += 1
    
    # Usual cumulative summation of counting sort alg
    for index in range(1, len(count_arr)):
        count_arr[index] += count_arr[index - 1]
    
    # Initialize a 0-array length of input array
    output_arr = [0] * len(arr)

    # For each element in the array (in reverse order);
    for r_index in range(len(arr)-1, -1, -1):
        # (arr[r_index] // exp) % 10 gives the value of
        # last digit, as explained in detail in line 11
        # Then we fetch the frequency (the position we 
        # should put the element into the output_arr)
        # from count_arr.
        position = count_arr[(arr[r_index] // exp) % 10]

        # Put the element element into the (position - 1)
        # The reason behind subtraction by 1 is, index system
        # is treated as if it starts by 1. Therefore, we subtract
        # by 1 while putting into the output_arr. Since value 0 in
        # the count_arr means that: 'there no left for this frequency'
        output_arr[position - 1] = arr[r_index]

        # Then we decrease the used frequency by 1
        count_arr[arr[r_index] // exp] -= 1
    
    # Since function does not return a value AND radix_sort func
    # does only apply the counting_sort func, we should record all
    # the changes onto the arr
    for i in range(len(arr)):
        arr[i] = output_arr[i]

def radix_sort(arr: List[int]) -> List[int]:
    """Radix Sort Algorithm (LSD)"""

    # Return array if it has 0 or 1 elements
    if len(arr) <= 1:
        return arr

    # Get the max element
    max_elem = max(arr)

    # Loop until max_element > exp
    exp = 1
    while max_elem >= exp:

        # Apply counting sort based on the
        # current digit
        counting_sort(arr, exp)

        # Add a 0 to exp
        exp *= 10
    
    # Return array
    return arr
