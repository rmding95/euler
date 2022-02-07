from typing import Iterator


def main():
    hexagon_set = set()
    pentagon_itr = pentagonal_nums()
    hexagon_itr = hexagonal_nums()
    for i in range(100000):
        hexagon_set.add(next(hexagon_itr))
        p_num = next(pentagon_itr)
        if p_num in hexagon_set:
            print(p_num)


def pentagonal_nums() -> Iterator[int]:
    n = 1
    while True:
        yield (n * (3 * n - 1)) // 2
        n += 1


def hexagonal_nums() -> Iterator[int]:
    n = 1
    while True:
        yield n * (2 * n - 1)
        n += 1


def triangle_nums() -> Iterator[int]:
    n = 1
    while True:
        yield (n * (n + 1)) // 2
        n += 1


if __name__ == "__main__":
    main()
