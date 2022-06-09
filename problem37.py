from util import get_digits, primes_up_to_n_optimized, timer

LIMIT = 1000000


@timer
def main():
    primes = primes_up_to_n_optimized(LIMIT)
    primes_cache = set(primes)
    ans: list[int] = []
    for p in primes:
        if p > LIMIT:
            break
        if p in (2, 3, 5, 7):
            continue
        if not is_truncatable_prime(p, primes_cache):
            continue
        ans.append(p)
    print(sum(ans))


def is_truncatable_prime(n: int, primes_cache: set[int]) -> bool:
    digits = get_digits(n)
    if len(digits) > 2 and any([x in (0, 2, 4, 6, 8) for x in digits]):
        return False

    n_copy = 0
    for i in range(len(digits) - 1):
        n_copy = n_copy + digits[i] * pow(10, i)
        if n_copy not in primes_cache:
            return False
    n_copy = 0
    for i in range(len(digits) - 1, 0, -1):
        n_copy = n_copy * 10 + digits[i]
        if n_copy not in primes_cache:
            return False
    return True


if __name__ == "__main__":
    main()
