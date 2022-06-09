from math import factorial

from util import get_digits, timer

LIMIT = int(1e7)


@timer
def main():
    ans = 0
    factorial_cache: dict[int, int] = {}
    for i in range(0, 10):
        factorial_cache[i] = factorial(i)
    for i in range(3, LIMIT):
        digits = get_digits(i)
        factorial_sum = sum([factorial_cache[x] for x in digits])
        if factorial_sum == i:
            ans += i
            print(i)


if __name__ == "__main__":
    main()
