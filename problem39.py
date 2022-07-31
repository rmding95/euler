from collections import defaultdict
from typing import DefaultDict


LIMIT = 1500000


def main():
    seen_tuples: set[frozenset[int]] = set()
    perimeter_to_tuple_map: DefaultDict[int, int] = defaultdict(int)
    for m in range(2, LIMIT + 1):
        for n in range(1, m):
            k = 1
            tup = frozenset(generate_pythagorean_tuple(m, n, k))
            sum_tup = sum(tup)
            if sum_tup > LIMIT:
                break
            if tup not in seen_tuples:
                perimeter_to_tuple_map[sum_tup] += 1
                seen_tuples.add(tup)
                while True:
                    k += 1
                    scaled_tup = frozenset(generate_pythagorean_tuple(m, n, k))
                    sum_scaled_tup = sum(scaled_tup)
                    if sum_scaled_tup > LIMIT:
                        break
                    else:
                        seen_tuples.add(scaled_tup)
                        perimeter_to_tuple_map[sum_scaled_tup] += 1
    # answer to problem 39
    print(max(perimeter_to_tuple_map, key=perimeter_to_tuple_map.__getitem__))
    # answer to problem 75
    print(len([x for x in perimeter_to_tuple_map.values() if x == 1]))


def generate_pythagorean_tuple(m: int, n: int, k: int) -> tuple[int, int, int]:
    return ((pow(m, 2) - pow(n, 2)) * k, (2 * m * n) * k, (pow(m, 2) + pow(n, 2)) * k)


if __name__ == "__main__":
    main()
