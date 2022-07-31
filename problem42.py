from typing import Iterator


def main():
    triangle_cache: set[int] = set()
    triangle_itr = triangle_nums()
    for _ in range(100):
        triangle_cache.add(next(triangle_itr))
    with open("p042_words.txt") as f:
        txt = f.read()
        words = txt.split(",")
        num_triangle_words = 0
        for word in words:
            word_sum = 0
            for c in word:
                if c in ('"', "'"):
                    continue
                word_sum += ord(c) - ord("A") + 1
            if word_sum in triangle_cache:
                num_triangle_words += 1
        print(num_triangle_words)


def triangle_nums() -> Iterator[int]:
    n = 1
    while True:
        yield (n * (n + 1)) // 2
        n += 1


if __name__ == "__main__":
    main()
