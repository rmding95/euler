from util import primes_up_to_n_optimized, prime_factorization


DISTINCT_PRIME_FACTORS = 4


def main():
    primes = primes_up_to_n_optimized(int(1e7))
    consecutive_factors = 0
    for i in range(100000, 1000000):
        pf = prime_factorization(i, primes)
        if len(pf) == DISTINCT_PRIME_FACTORS:
            consecutive_factors += 1
        else:
            consecutive_factors = 0
        if consecutive_factors == DISTINCT_PRIME_FACTORS:
            print(i)
            break


if __name__ == "__main__":
    main()
