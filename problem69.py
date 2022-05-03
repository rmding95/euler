from collections import defaultdict
from math import gcd
from typing import DefaultDict

from util import prime_factorization, timer, primes_up_to_n_optimized

LIMIT = 100000


@timer
def main():
    primes = primes_up_to_n_optimized(LIMIT)
    primes_cache = set(primes)
    phi_cache: dict[int, int] = {}
    factorization_cache: dict[int, set[int]] = {}
    factors_to_nums_cache: DefaultDict[int, set[int]] = defaultdict(set)
    for i in range(1, LIMIT + 1):
        pf = prime_factorization(i, primes)
        factorization_cache[i] = set([x[0] for x in pf])
        for tup in pf:
            factors_to_nums_cache[tup[0]].add(i)
    max_ratio = 0
    ans = 0
    cache_count = 0
    for i in range(2, LIMIT):
        if i in phi_cache:
            cache_count += 1
            phi = phi_cache[i]
        else:
            phi, coprimes = euler_totient_func(i, primes_cache, factorization_cache, factors_to_nums_cache)
            phi_cache[i] = phi
            # calculate_multiplicative_values(i, phi, coprimes, phi_cache)
        ratio = i / phi
        if ratio > max_ratio:
            max_ratio = ratio
            ans = i
    print(f"max n: {ans} with ratio {max_ratio}")
    print(cache_count)
    # for i in range(1, 10):
    #     phi, coprimes = euler_totient_func(100000, primes_cache, factorization_cache)
    #     phi_cache[i] = phi
    #     calculate_multiplicative_values(i, phi, coprimes, phi_cache)


def is_coprime(a: int, b: int) -> bool:
    return gcd(a, b) == 1


def euler_totient_func(
    n: int, primes_cache: set[int], factorization_cache: dict[int, set[int]], factors_cache: DefaultDict[int, set[int]]
) -> tuple[int, list[int]]:
    """
    Counts the positive integers up to N that are coprime to N
    """
    if n == 1:
        return 1, [1]
    # primes are coprime with all integers < N
    if n in primes_cache:
        return n - 1, list(range(1, n))
    count = 1
    coprimes = [1]
    prime_factors_n = factorization_cache[n]
    # for factor in factors_cache:
    #     if factor in prime_factors_n:
    #         continue
    #     for nums in factors_cache[factor]:
    #         if prime_factors_n.isdisjoint(factorization_cache[nums]):
    #             count += 1
    #             coprimes.append(nums)
    for i in range(2, n):
        prime_factors_i = factorization_cache[i]
        if prime_factors_n.isdisjoint(prime_factors_i):
            count += 1
            coprimes.append(i)
    return count, coprimes


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
    return


if __name__ == "__main__":
    main()
