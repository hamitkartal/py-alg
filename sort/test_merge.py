from merge import *

def test_intertwine():
    
    # both arrays have same length, elements are interleaved
    assert intertwine([1,3,5], [2,4,6]) == [1,2,3,4,5,6]
    
    # one array is longer than other
    assert intertwine([1,2,3], [4,5,6,7,8]) == [1,2,3,4,5,6,7,8]

    # both arrays are empty
    assert intertwine([], []) == []

    # one array is empty
    assert intertwine([1,2,3], []) == [1,2,3]

    # arrays with duplicate elements
    assert intertwine([1,3,3], [2,3,4]) == [1,2,3,3,3,4]

    # arrays with negative and positive numbers
    assert intertwine([-3, -1, 0, 2], [-2, 1, 3]) == [-3, -2, -1, 0, 1, 2, 3]

    # both arrays contain the same elements
    assert intertwine([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]

    # arrays are already sorted in descending order
    assert intertwine([5, 3, 1], [6, 4, 2]) == [5, 3, 1, 6, 4, 2]

    # arrays of different lengths, with no common elements
    assert intertwine([1, 5, 9], [2, 6, 10, 12, 14]) == [1, 2, 5, 6, 9, 10, 12, 14]

    # arrays with a single element each
    assert intertwine([1], [2]) == [1, 2]


def test_merge_sort():
    pass
    # array with multiple elements in random order
    assert merge_sort([4, 1, 7, 3, 8, 2, 5, 6]) == [1, 2, 3, 4, 5, 6, 7, 8]

    # already sorted array
    assert merge_sort([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]

    # reverse-sorted array
    assert merge_sort([8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8]

    # array with duplicate elements
    assert merge_sort([3, 1, 2, 3, 1, 2, 3]) == [1, 1, 2, 2, 3, 3, 3]

    # array with a single element
    assert merge_sort([5]) == [5]

    # empty array
    assert merge_sort([]) == []

    # array with negative and positive numbers
    assert merge_sort([-1, 2, -3, 4, -5, 6, -7, 8]) == [-7, -5, -3, -1, 2, 4, 6, 8]

    # array with all identical elements
    assert merge_sort([2,2,2,2,2]) == [2,2,2,2,2]

    # array with elements in an alternating high-low pattern
    assert merge_sort([5, 1, 6, 2, 7, 3, 8, 4]) == [1, 2, 3, 4, 5, 6, 7, 8]
