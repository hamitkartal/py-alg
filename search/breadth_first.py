from typing import List


def breadth_first_search(graph: List[List[int]], start_node):

    # Initialize an empty array for visited nodes
    visited = []
    # Initialize a queue (a list tbh) for queue
    queue = [start_node]

    # Loop until queue is empty, means we can't
    # traverse more
    while len(queue) != 0:

        # Take the next node in the queue
        next_node = queue.pop(0)

        # If node is not visited
        if next_node not in visited:

            # Then append it to the visited
            # i.e visit it
            visited.append(next_node)

            # For each adjacent,
            for adjacent in graph[next_node]:

                # If adjacent not visited,
                if adjacent not in visited:

                    # Enqueue it to the queue
                    # for future (possible) visits
                    queue.append(adjacent)
    return visited
