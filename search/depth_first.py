from typing import List


def depth_first_search(graph: List[List[int]], start_node=0):
    visited = []
    stack = [start_node]
    while len(stack) != 0:
        next_to_visit = stack.pop()
        if next_to_visit not in visited:
            visited.append(next_to_visit)
            for adjacent in graph[next_to_visit]:
                if adjacent not in stack:
                    stack.append(adjacent)
    return visited
