from linear import linear_search

def test_linear_search():

    # target present in the middle
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 4

    # target not present
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == -1

    # target present at the beginning
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 0

    # target present at the end
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 8

    # empty array
    assert linear_search([], 3) == -1

    # single-element array, target present
    assert linear_search([5], 5) == 0

    # single-element array, target not present
    assert linear_search([5], 3) == -1

    # target present in array, with negative numbers
    assert linear_search([-10, -5, 0, 5, 10, 15, 20], -5) == 1

    # target present in array with repeated elements
    assert linear_search([1, 1, 2, 2, 2, 3, 3], 2) == 2

    # large array, target present
    assert linear_search(list(range(1000)), 456) == 456

    # large array, target not present
    assert linear_search(list(range(1000)), -1000) == -1
