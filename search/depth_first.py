from typing import List


def depth_first_search(graph: List[List[int]], start_node=0):

    # Initially, create an empty visited list
    visited = []
    # and a stack with starting node
    stack = [start_node]

    # Loop until stack is empty
    while len(stack) != 0:

        # Pop the last element from the stack
        next_to_visit = stack.pop()

        # If it's already visited, skip it
        if next_to_visit not in visited:

            # If not, then append to visited
            visited.append(next_to_visit)

            # For each adjacents of the node,
            for adjacent in graph[next_to_visit]:

                # If not added to stack previously,
                if adjacent not in stack:

                    # Append to stack
                    stack.append(adjacent)

    # Then return the visited (output) list
    return visited
