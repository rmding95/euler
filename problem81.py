from collections import defaultdict
from heapq import heappush, heappop
from math import inf
from typing import DefaultDict


def main():
    matrix: list[list[int]] = []
    with open("test_matrix.txt") as f:
        for line in f.readlines():
            if len(line) == 0:
                continue
            inner: list[int] = []
            for v in line.split(","):
                inner.append(int(v))
            matrix.append(inner)
    res = a_star((0, 0), (4, 4), matrix)
    print(res)


def a_star(start: tuple[int, int], end: tuple[int, int], matrix: list[list[int]]) -> list[tuple[int, int]]:
    """A* shortest path using the value of each index as the distance function
    NOTE: for problem 81 we are only exploring down and right as neighbors"""
    # a min-heap of discovered nodes
    discovered_nodes: list[tuple[float, tuple[int, int]]] = []
    # for (row, col), came_from[(row, col)] is the index immediately preceding it on shortest path
    came_from: dict[tuple[int, int], tuple[int, int]] = {}
    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    g_score: DefaultDict[tuple[int, int], float] = defaultdict(lambda: inf)
    # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    # how cheap a path could be from start to finish if it goes through n.
    f_score: DefaultDict[tuple[int, int], float] = defaultdict(lambda: inf)
    f_score[start] = matrix[start[0]][start[1]]
    heappush(discovered_nodes, (matrix[start[0]][start[1]], start))

    while len(discovered_nodes) != 0:
        current_node = heappop(discovered_nodes)
        current_idx = current_node[1]
        if current_node == end:
            total_path = [current_idx]
            while current_idx in came_from.keys():
                current_idx = came_from[current_idx]
                total_path.append(current_idx)
            return total_path
        neighbors = [(current_idx[0] + 1, current_idx[1]), (current_idx[0], current_idx[1] + 1)]
        for neighbor in neighbors:
            if neighbor[0] >= len(matrix):
                continue
            if neighbor[1] >= len(matrix[current_idx[0]]):
                continue
            tentative_score = g_score[current_idx] + matrix[neighbor[0]][neighbor[1]]
            if tentative_score < g_score[neighbor]:
                came_from[neighbor] = current_idx
                g_score[neighbor] = tentative_score
                f_score[neighbor] = tentative_score
                neighbor_tup = (tentative_score, neighbor)
                if neighbor_tup not in discovered_nodes:
                    heappush(discovered_nodes, neighbor_tup)
    return []


if __name__ == "__main__":
    main()
