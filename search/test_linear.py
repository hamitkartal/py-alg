from linear import linear_search

def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 4
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == -1
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 0
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 8
    assert linear_search([], 3) == -1
    assert linear_search([5], 5) == 0
    assert linear_search([5], 3) == -1
    assert linear_search([-10, -5, 0, 5, 10, 15, 20], -5) == 1
    assert linear_search([1, 1, 2, 2, 2, 3, 3], 2) == 2
    assert linear_search(list(range(1000)), 456) == 456
    assert linear_search(list(range(1000)), -1000) == -1
