from collections import defaultdict
from typing import DefaultDict


LIMIT = 1000


def main():
    seen_tuples: set[tuple[int, int, int]] = set()
    perimeter_to_tuple_map: DefaultDict[int, int] = defaultdict(int)
    for m in range(2, LIMIT + 1):
        for n in range(1, m):
            k = 1
            tup = generate_pythagorean_tuple(m, n, k)
            sum_tup = sum(tup)
            if sum_tup > LIMIT:
                break
            if tup not in seen_tuples:
                perimeter_to_tuple_map[sum_tup] += 1
                seen_tuples.add(tup)
                while True:
                    k += 1
                    scaled_tup = generate_pythagorean_tuple(m, n, k)
                    sum_scaled_tup = sum(scaled_tup)
                    if sum_scaled_tup > LIMIT:
                        break
                    else:
                        seen_tuples.add(scaled_tup)
                        perimeter_to_tuple_map[sum_scaled_tup] += 1
    print(max(perimeter_to_tuple_map, key=perimeter_to_tuple_map.__getitem__))


def generate_pythagorean_tuple(m: int, n: int, k: int) -> tuple[int, int, int]:
    return ((pow(m, 2) - pow(n, 2)) * k, (2 * m * n) * k, (pow(m, 2) + pow(n, 2)) * k)


if __name__ == "__main__":
    main()
