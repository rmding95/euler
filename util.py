from collections import defaultdict
from functools import wraps
from itertools import product
from math import gcd, sqrt, prod
from random import randint
from time import time
from typing import Callable


def primes_up_to_n_optimized(n: int) -> list[int]:
    """Uses an optimized sieve of erathsthenes which only accounts for odd numbers
    the ith element of sieve corresponds to 2i+1
    iterate from 2i(i+1) by steps of 2i+1
    """
    sieve_bound = int((n - 1) / 2)
    product_bound = int((sqrt(n) - 1) / 2)
    sieve = [False] * sieve_bound
    for i in range(1, product_bound):
        if sieve[i]:
            continue
        for j in range(2 * i * (i + 1), sieve_bound, 2 * i + 1):
            sieve[j] = True
    # 2 is the only non-odd prime
    primes = [2]
    primes.extend([(idx * 2 + 1,)[0] for idx, val in enumerate(sieve) if not val][1:])
    return primes


def prime_factorization(n: int, primes: list[int]) -> list[tuple[int, int]]:
    """A first try at a prime factorization algorithm
    1. Cacluate all primes up to n
    2. Perform trial division using primes to find the bases
        - if n % p == 0, then compute n /= p and add one to the power of p
    """
    if n == 1:
        return [(1, 1)]
    factorization = []
    for prime in primes:
        if prime > n:
            break
        if n % prime != 0:
            continue
        power_of_prime = 0
        while n % prime == 0:
            n //= prime
            power_of_prime += 1
        factorization.append((prime, power_of_prime))
    if n > 1:
        factorization.append((n, 1))
    return factorization


def print_factorization(n: int, factorization: list[tuple[int, int]]) -> str:
    s = f"prime factorization of {n}: {factorization[0][0]}^{factorization[0][1]}"
    for tup in factorization[1:]:
        s += f" * {tup[0]}^{tup[1]}"
    return s


def count_num_factors_from_prime_factorization(pf: list[tuple[int, int]]) -> int:
    """Returns how many factors a number has based on its prime factorization
    The number of factors is equal to the size of the cartesian product between sets of size 1+power"""
    product = 1
    for tup in pf:
        product *= tup[1] + 1
    return product


def get_divisors_from_prime_factorization(pf: list[tuple[int, int]]) -> list[int]:
    """Given a prime factorization of the form: [ (prime, power), ...], return a list of all divisors of n"""
    divisors = []
    multiples = []
    for prime, power in pf:
        multiples.append([pow(prime, i) for i in range(power + 1)])
    for v in product(*multiples):
        divisors.append(prod(v))
    return divisors


def pollard_rho_prime_factorization(n: int, primes: list[int]) -> list[tuple[int, int]]:
    primes_cache = set(primes)
    if n in primes_cache:
        return [1, n]
    # if n <= int(1e8):
    #     return prime_factorization(n, primes)
    n_copy = n
    factorization = defaultdict(int)
    while n_copy > int(1e8):
        print(f"starting iteration with {n_copy}")
        factors = set()
        for _ in range(100):
            factor = _pollard_rho(n_copy)
            if factor != -1:
                factors.add(factor)
        if len(factors) == 0:
            print(f"{n_copy} is prime")
            factorization[n_copy] += 1
            return [(factor, power) for factor, power in factorization.items()]
        prime_factors = [x for x in factors if x in primes_cache]

        factorization_start_factors = prime_factors if len(prime_factors) > 0 else sorted(list(factors))
        for factor in factorization_start_factors:
            if factor > n_copy:
                break
            if n_copy % factor != 0:
                continue
            while n_copy % factor == 0:
                n_copy //= factor
                factorization[factor] += 1
    if n_copy > 1:
        pf = prime_factorization(n_copy, primes)
        for tup in pf:
            factorization[tup[0]] += tup[1]
    return [(factor, power) for factor, power in factorization.items()]


def _pollard_rho(n: int, max_iters: int = 1000) -> int:
    """Uses the pollard rho algorithm to return either one valid factor (or -1 if max_iters is exceeded)"""

    def _rand_func(f: int, c: int) -> int:
        return (f * f + 1) % c

    a = randint(2, n * n)
    b = 2
    d = 1
    iters = 0
    while d == 1:
        a = _rand_func(a, n)
        b = _rand_func(_rand_func(b, n), n)
        d = gcd((a - b), n)
        iters += 1
        if iters > max_iters:
            return -1
    if d == n:
        return -1
    else:
        return d


def test_primes_from_file(filename: str) -> None:
    primes = []
    with open(filename) as f:
        for line in f.readlines():
            split = line.split()
            for prime in split:
                primes.append(int(prime))
    # the 1000th prime is 7919
    my_primes = primes_up_to_n_optimized(7921)
    assert len(primes) == len(my_primes)
    assert primes == my_primes
    print("all good!")


def timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper():
        tic = time()
        func()
        print(f"Runtime {time() - tic} seconds")

    return wrapper


def get_digits(n: int) -> list[int]:
    digits: list[int] = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits


def is_prime(n: int) -> bool:
    """A deterministic Miller-Rabin test based off testing specific witness numbers depending on N"""
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n < 2047:
        witnesses = [2]
    elif n < 1373653:
        witnesses = [2, 3]
    elif n < 1122004669633:
        witnesses = [2, 13, 23, 1662803]
    elif n < pow(2, 64):
        witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    elif n < 3317044064679887385961981:
        witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    else:
        raise Exception(f"{n} is too large for this implementation")
    powers_of_two = 0
    n_copy = n - 1
    while n_copy % 2 == 0:
        n_copy //= 2
        powers_of_two += 1
    # print(f"{n} can be written as 2^{powers_of_two} * {n_copy} + 1")
    for witness in witnesses:
        x = pow(witness, n_copy, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(powers_of_two - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        if x == n - 1:
            continue
        return False
    return True


def tuple_to_int(t: tuple[int, ...]) -> int:
    """Convert a tuple like (1, 2, 3) to an int,assuming the greatest digit
    is the left-most, this example would return 123"""
    t_len = len(t)
    num = 0
    for i in range(t_len):
        num += pow(10, t_len - i - 1) * t[i]
    return num
