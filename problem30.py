from util import print_factorization, prime_factorization, primes_up_to_n_optimized

POWER = 4


def main():
    primes = primes_up_to_n_optimized(10001)
    nums = [1634, 8208, 9474]
    for num in nums:
        pf = prime_factorization(num, primes)
        print(print_factorization(num, pf))


if __name__ == "__main__":
    main()
