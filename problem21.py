import time

from util import (
    primes_up_to_n_optimized,
    prime_factorization,
    get_divisors_from_prime_factorization,
)


UPPER_LIMIT = 10000


def main():
    tic = time.time()
    primes = primes_up_to_n_optimized(10003)

    cache = {}
    for i in range(UPPER_LIMIT):
        pf = prime_factorization(i, primes)
        div = get_divisors_from_prime_factorization(pf)
        cache[i] = sum(div) - i

    amicable_numbers = []
    for num in cache:
        if num in amicable_numbers:
            continue
        d_n = cache[num]
        if d_n != num and d_n in cache and cache[d_n] == num:
            amicable_numbers.append(num)
            amicable_numbers.append(d_n)
    print(sum(amicable_numbers))

    print(time.time() - tic)


if __name__ == "__main__":
    main()
