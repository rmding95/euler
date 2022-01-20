import time

from util import (
    primes_up_to_n_optimized,
    pollard_rho_prime_factorization,
    prime_factorization,
    print_factorization,
    count_num_factors_from_prime_factorization,
)

UPPER_LIMIT = int(1e15)


def main():
    tic = time.time()
    primes = []
    with open("euler/primes_up_to_1e8.txt") as f:
        text = f.read().rstrip()
        primes = text.split(" ")
        primes = [int(x) for x in primes]

    current_num = 0
    ith_triangle_num = 0
    while current_num < UPPER_LIMIT:
        current_num += ith_triangle_num
        ith_triangle_num += 1
        if current_num > int(7e7) and current_num % 10 == 0:
            pf = pollard_rho_prime_factorization(current_num, primes)
            num_factors = count_num_factors_from_prime_factorization(pf)
            print(f"pf of {current_num}: {pf}, num factors: {num_factors}")
            if num_factors > 500:
                return current_num
    # pf = pollard_rho_prime_factorization(600851475143, primes)
    # print(pf)
    print(f"runtime: {time.time() - tic}")


if __name__ == "__main__":
    main()
