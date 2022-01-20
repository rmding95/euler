import time

from util import prime_factorization, get_divisors_from_prime_factorization, primes_up_to_n_optimized

UPPER_LIMIT = 28123


def main():
    tic = time.time()
    primes = primes_up_to_n_optimized(UPPER_LIMIT * 2)

    abundant_nums = set()
    for i in range(1, UPPER_LIMIT + 1):
        pf = prime_factorization(i, primes)
        divisors = get_divisors_from_prime_factorization(pf)
        sum_divisors = sum(divisors) - i
        if sum_divisors > i:
            abundant_nums.add(i)
    # print(abundant_nums)
    ans = set()
    for i in range(UPPER_LIMIT, 0, -1):
        pair_found = False
        for n in abundant_nums:
            if n > i:
                continue
            n_2 = i - n
            if n_2 in abundant_nums:
                # print(f"{i}, {n}, {n_2}")
                pair_found = True
        if not pair_found and i not in ans:
            ans.add(i)
    print(sum(ans))
    print(time.time() - tic)


if __name__ == "__main__":
    main()
