from typing import Optional

from util import get_digits, primes_up_to_n_optimized, timer

LIMIT = 1000001


class Node:

    value: int
    next: Optional["Node"]

    def __init__(self, value: int):
        self.value = value
        self.next = None


@timer
def main():
    primes_cache = set(primes_up_to_n_optimized(LIMIT))
    seen_nums: set[int] = set()
    ans_set: set[int] = set([2])
    for i in range(LIMIT):
        if i in seen_nums or i in ans_set or i not in primes_cache:
            continue
        rotations = get_rotations(i)
        if not rotations:
            seen_nums.add(i)
            continue
        if all([x in primes_cache for x in rotations]):
            ans_set.update(rotations)
        else:
            seen_nums.update(rotations)
    print(sorted(ans_set))
    print(len(ans_set))


def get_rotations(n: int) -> Optional[list[int]]:
    digits = get_digits(n)
    digits.reverse()
    for even_digit in (0, 2, 4, 6, 8):
        if even_digit in digits:
            return None
    rotations: list[int] = []
    # start_node = Node(digits[0])
    # current_node = start_node
    # for i in range(1, len(digits)):
    #     next_node = Node(digits[i])
    #     current_node.next = next_node
    #     current_node = next_node
    # current_node.next = start_node
    # for i in range(len(digits)):
    #     current = start_node
    #     num = 0
    #     for j in range(len(digits)):
    #         num += pow(10, len(digits) - j - 1) * current.value
    #         current = current.next
    #     start_node = start_node.next
    #     rotations.append(num)
    for _ in range(len(digits)):
        current_idx = 0
        current_val = digits[current_idx]
        for _ in range(0, len(digits)):
            next_idx = (current_idx + 1) % len(digits)
            next_num = digits[next_idx]
            digits[next_idx] = current_val
            current_val = next_num
            current_idx = next_idx
        rotations.append(int("".join([str(x) for x in digits])))
    return rotations


if __name__ == "__main__":
    main()
