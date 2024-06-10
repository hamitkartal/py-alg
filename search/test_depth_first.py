from depth_first import depth_first_search


def test_depth_first_search():

    # Linear Graph
    graph = [[1], [0, 2], [1, 3], [2]]
    expected = [0, 1, 2, 3]
    assert depth_first_search(graph) == expected

    # Graph with cycles
    graph = [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]
    expected = [0, 2, 3, 1]
    assert depth_first_search(graph) == expected

    # Disconnected graph
    graph = [[1], [0], [3], [2]]
    expected = [0, 1]
    assert depth_first_search(graph) == expected

    graph = [[1, 2, 3], [0], [0, 4, 3], [0, 2], [2]]
    expected =  [0, 3, 2, 4, 1]
    assert depth_first_search(graph) == expected
