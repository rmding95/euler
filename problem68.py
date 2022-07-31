from itertools import permutations

from util import timer

LINE_LEN = 3


class NGonRing:
    def __init__(self, n: int):
        self.size = n
        self.lines: list[list[int]] = []
        self.total_nodes = n * LINE_LEN - n

    def enumerate_possibilities(self) -> set[int]:
        possible_numbers = range(1, self.total_nodes + 1)
        possible_set = set(possible_numbers)
        center_combinations = permutations(possible_numbers, self.size)
        cache: set[int] = set()
        for c in center_combinations:
            possible_subset = possible_set.difference(c)
            possible_sums = []
            for i in range(len(c)):
                if i == len(c) - 1:
                    possible_sums.append(c[i] + c[0])
                else:
                    possible_sums.append(c[i] + c[i + 1])
            edge_nodes = self.check_final_node_possibilities(possible_sums, possible_subset)
            if len(edge_nodes) > 0:
                answers = self.print_answer(c, edge_nodes)
                cache.update(answers)
        return cache

    def check_final_node_possibilities(self, start_nums: list[int], possible_nums: set[int]) -> list[tuple[int, ...]]:
        """Given a list 'start_nums' which represents the sum of the two center nodes of each line,
        and a set of possible nums of numbers which can still be used, find valid possibilities"""
        valid: list[tuple[int, ...]] = []
        for p in permutations(possible_nums, len(possible_nums)):
            target_sum = start_nums[0] + p[0]
            valid_combination = True
            for i in range(1, len(p)):
                if start_nums[i] + p[i] != target_sum:
                    valid_combination = False
            if valid_combination:
                valid.append(p)
        return valid

    def print_answer(self, center_nodes: tuple[int, ...], edge_nodes: list[tuple[int, ...]]) -> list[int]:
        """Given the set of center nodes and edge nodes, return a 9-digit string in the expected answer format
        Example: given center nodes of (1,2,3) and edge nodes of (6,4,5), return 423531612
        """
        answers: list[int] = []
        for edge_node in edge_nodes:
            edge_start_idx = edge_node.index(min(edge_node))
            s = ""
            for i in range(len(edge_node)):
                s += str(edge_node[(i + edge_start_idx) % len(edge_node)])
                for j in range(LINE_LEN - 1):
                    s += str(center_nodes[(j + i + edge_start_idx) % len(center_nodes)])
            answers.append(int(s))
        return answers


@timer
def main():
    ring = NGonRing(5)
    answers = ring.enumerate_possibilities()
    print(sorted([x for x in answers if len(str(x)) == 16], reverse=True)[0])


if __name__ == "__main__":
    main()
