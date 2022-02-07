from itertools import permutations

from util import primes_up_to_n_optimized


def main():
    primes = primes_up_to_n_optimized(10001)
    four_digit_primes = [x for x in primes if len(str(x)) == 4]
    checked = set()
    for prime in four_digit_primes:
        if prime in checked:
            continue
        perms = list(permutations(str(prime), 4))
        nums = set([int("".join(x)) for x in perms])
        prime_nums = [x for x in nums if x in four_digit_primes]
        for n in prime_nums:
            checked.add(n)
        if len(prime_nums) > 2:
            prime_nums = sorted(prime_nums)
            for i in range(len(prime_nums) - 1):
                for j in range(i + 1, len(prime_nums)):
                    diff = prime_nums[j] - prime_nums[i]
                    if prime_nums[j] + diff in prime_nums:
                        print(prime_nums[i], prime_nums[j], prime_nums[j] + diff)


if __name__ == "__main__":
    main()
