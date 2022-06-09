from collections import defaultdict
from math import gcd
from typing import DefaultDict

from util import prime_factorization, timer, primes_up_to_n_optimized

LIMIT = 10


@timer
def main():
    primes = primes_up_to_n_optimized(LIMIT + 1)
    primes_cache = set(primes)
    phi_cache: dict[int, int] = {}
    factorization_cache: dict[int, tuple[int, ...]] = {}
    prime_factors_to_coprimes_cache: DefaultDict[
        tuple[int, ...], list[int]
    ] = defaultdict(list)
    for i in range(1, LIMIT + 1):
        pf = prime_factorization(i, primes)
        factorization_cache[i] = tuple([x[0] for x in pf])
        # prime_factors = tuple([x[0] for x in pf])
        # prime_factors_to_coprimes_cache[prime_factors].append(i)
    max_ratio = 0
    ans = 0
    cache_count = 0

    # for i in range(LIMIT, LIMIT - (LIMIT // 10), -1):
    #     phi, _ = euler_totient_func(
    #         i, primes_cache, factorization_cache, prime_factors_to_coprimes_cache
    #     )
    #     phi_cache[i] = phi
    #     ratio = i / phi
    #     if ratio > max_ratio:
    #         max_ratio = ratio
    #         ans = i

    for i in range(2, LIMIT + 1):
        if i in phi_cache:
            cache_count += 1
            phi = phi_cache[i]
        elif i in primes_cache:
            # primes are coprime with all integers < N
            phi = i - 1
            phi_cache[i] = phi
        else:
            phi, coprimes = euler_totient_func(
                i, primes_cache, factorization_cache, prime_factors_to_coprimes_cache
            )
            print(
                (
                    f"{i}\n"
                    f"prime factors: {factorization_cache[i]}\n"
                    f"coprimes: {coprimes}\n"
                    f"phi: {phi}\n"
                )
            )
            phi_cache[i] = phi
            calculate_multiplicative_values(i, phi, coprimes, phi_cache)
        ratio = i / phi
        if ratio > max_ratio:
            max_ratio = ratio
            ans = i
    print(f"max n: {ans} with ratio {max_ratio}")
    print(cache_count)
    # for i in range(1, LIMIT + 1):
    #     phi, coprimes = euler_totient_func(i, primes_cache, factorization_cache)
    #     phi_cache[i] = phi
    #     print(
    #         (
    #             f"{i}\n"
    #             f"prime factors: {factorization_cache[i]}\n"
    #             f"coprimes: {coprimes}\n"
    #             f"phi: {phi}\n"
    #         )
    #     )
    # calculate_multiplicative_values(i, phi, coprimes, phi_cache)


def is_coprime(a: int, b: int) -> bool:
    return gcd(a, b) == 1


def euler_totient_func(
    n: int,
    primes_cache: set[int],
    factorization_cache: dict[int, tuple[int, ...]],
    prime_factors_to_coprimes_cache: DefaultDict[tuple[int, ...], list[int]],
) -> tuple[int, list[int]]:
    """
    Counts the positive integers up to N that are coprime to N
    """
    # print(f"{n}: {prime_factors_to_coprimes_cache}")
    if n == 1:
        return 1, [1]
    prime_factors_n = factorization_cache[n]
    if prime_factors_n in prime_factors_to_coprimes_cache:
        coprimes = [
            x for x in prime_factors_to_coprimes_cache[prime_factors_n] if x < n
        ]
        return len(coprimes), coprimes

    prime_factors_n_set = set(prime_factors_n)
    count = 1
    coprimes: list[int] = []
    for i in range(1, n):
        prime_factors_i = factorization_cache[i]
        if prime_factors_n_set.isdisjoint(prime_factors_i):
            count += 1
            coprimes.append(i)
    if prime_factors_n not in prime_factors_to_coprimes_cache:
        prime_factors_to_coprimes_cache[prime_factors_n] = coprimes
    # prime_factors_n = factorization_cache[n]
    # print(prime_factors_n)
    # print(prime_factors_to_coprimes_cache)
    # coprimes = [x for x in prime_factors_to_coprimes_cache[prime_factors_n] if x < n]
    # print(coprimes)
    # for factor in factors_cache:
    #     if factor in prime_factors_n:
    #         continue
    #     for nums in factors_cache[factor]:
    #         if prime_factors_n.isdisjoint(factorization_cache[nums]):
    #             count += 1
    #             coprimes.append(nums)
    # for i in range(2, n):
    #     prime_factors_i = factorization_cache[i]
    #     if prime_factors_n.isdisjoint(prime_factors_i):
    #         count += 1
    #         coprimes.append(i)
    return len(coprimes), coprimes


def calculate_multiplicative_values(
    n: int, phi: int, coprimes: list[int], cache: dict[int, int]
) -> None:
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
