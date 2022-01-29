from collections import defaultdict
from typing import DefaultDict

from util import prime_factorization, print_factorization, primes_up_to_n_optimized

LIMIT = 100


def main():
    cache: DefaultDict[int, list[tuple[int, int]]] = defaultdict(list)
    primes = primes_up_to_n_optimized(LIMIT * LIMIT)
    for a in range(2, LIMIT + 1):
        for b in range(2, LIMIT + 1):
            prod = pow(a, b)
            cache[prod].append((a, b))
    # for k, v in cache.items():
    #     if len(v) > 1:
    #         print(f"{k}: {v}")
    #         pf = prime_factorization(k, primes)
    #         print(print_factorization(k, pf))
    #         print("\n\n")
    print(len(cache))


if __name__ == "__main__":
    main()
