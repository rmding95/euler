from typing import Iterator


def main():
    f = fib()
    for idx, val in enumerate(f):
        if len(str(val)) == 1000:
            print(idx)
            break


def fib() -> Iterator[int]:
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    main()
