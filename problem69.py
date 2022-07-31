from collections import defaultdict
from math import gcd
from typing import DefaultDict

from util import prime_factorization, timer, primes_up_to_n_optimized

LIMIT = 10000


@timer
def main():
    primes = primes_up_to_n_optimized(LIMIT + 1)
    primes_cache = set(primes)
    # cache of n to euler_totient_func(n)
    phi_cache: dict[int, int] = {}

    max_ratio = 0
    max_n = 0
    for i in range(2, LIMIT):
        if i in primes_cache:
            phi = i - 1
            phi_cache[i] = phi
        elif i in phi_cache:
            phi = phi_cache[i]
        else:
            coprimes = euler_totient_func(i)
            phi = len(coprimes)
            phi_cache[i] = phi
            calculate_multiplicative_values(i, phi, coprimes, phi_cache)
        ratio = i / phi
        if ratio > max_ratio:
            max_ratio = ratio
            max_n = i
    print(f"{max_n}: {max_ratio}")


def euler_totient_func(n: int) -> list[int]:
    """Returns the number of numbers less than n which are coprime to n"""
    coprimes: list[int] = []
    for i in range(1, n):
        if is_coprime(i, n):
            coprimes.append(i)
    return coprimes


def is_coprime(a: int, b: int) -> bool:
    return gcd(a, b) == 1


def calculate_multiplicative_values(n: int, phi: int, coprimes: list[int], cache: dict[int, int]) -> None:
    """
    Use the fact that euler's totient function is multiplicative,
    given gcd(m, n) = 1 then phi(m)*phi(n) = phi(m*n)
    """
    for coprime in coprimes:
        multiple = n * coprime
        if multiple > LIMIT:
            return
        if multiple <= n or multiple in cache:
            continue
        # assert n in cache, n
        # assert coprime in cache, coprime
        cache[multiple] = cache[n] * cache[coprime]


if __name__ == "__main__":
    main()
