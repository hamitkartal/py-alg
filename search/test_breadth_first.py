from breadth_first import breadth_first_search


def test_bfs():
    graph1 = [[1, 2, 3], [0], [0, 4, 3], [0, 2], [2]]
    assert breadth_first_search(graph1, 0) == [0, 1, 2, 3, 4]

    graph2 = [[1, 2], [0, 3], [0, 3], [1, 2]]
    assert breadth_first_search(graph2, 0) == [0, 1, 2, 3]

    graph3 = [[1], [2], [3], []]
    assert breadth_first_search(graph3, 0) == [0, 1, 2, 3]

    graph4 = [[], [2], [3], [1]]
    assert breadth_first_search(graph4, 1) == [1, 2, 3]

    graph5 = [[1], [0, 2, 3], [1, 3, 4], [1, 2], [2]]
    assert breadth_first_search(graph5, 0) == [0, 1, 2, 3, 4]
