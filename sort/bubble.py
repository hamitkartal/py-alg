from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """Bubble Sort Algorithm"""

    # Return array immediately if has
    # less than 1 elements
    if len(arr) <= 1:
        return arr
    
    # Initialize barrier pointer as
    # being pointing to the last element
    barrier_ptr = len(arr) - 1

    # While barrier pointer not pointing
    # to the first element,
    while barrier_ptr > 0:

        # Send a traveler pointer until the barrier ptr
        for traveler_ptr in range(barrier_ptr):

            # If the current element is bigger than the next one
            if arr[traveler_ptr] > arr[traveler_ptr + 1]:

                # swap them
                arr[traveler_ptr], arr[traveler_ptr + 1] = arr[traveler_ptr + 1], arr[traveler_ptr]
        
        # Make the barrier pointer next last element
        barrier_ptr -= 1
    
    # Return the array itself
    return arr
