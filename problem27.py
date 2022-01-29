from typing import Iterator
from util import primes_up_to_n_optimized


LIMIT = 1000


def quadratic(a: int, b: int) -> Iterator[int]:
    n = 0
    while True:
        yield (n * n) + (a * n) + b
        n += 1


def main():
    primes = set(primes_up_to_n_optimized(1001))
    max_prime_count = 0
    ans = ()
    for a in range(-LIMIT, LIMIT):
        for b in range(-LIMIT, LIMIT + 1):
            prime_count = 0
            for v in quadratic(a, b):
                if v not in primes:
                    if prime_count > max_prime_count:
                        max_prime_count = prime_count
                        ans = (a, b)
                    break
                prime_count += 1
    print(max_prime_count)
    print(ans)


if __name__ == "__main__":
    main()
