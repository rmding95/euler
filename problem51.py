from itertools import combinations

from util import primes_up_to_n_optimized

DIGITS = 6


def main():
    primes = primes_up_to_n_optimized(int(1e7))
    max_family_size = 0
    ans = []
    for i in range(DIGITS, DIGITS + 1):
        primes = [x for x in primes if len(str(x)) == i]
        primes_cache = set(primes)
        visited = {}
        for j in range(1, DIGITS):
            for tup in combinations(range(DIGITS), j):
                for p in primes:
                    replacements = get_replacements(p, tup)
                    prime_replacements = primes_cache.intersection(replacements)
                    if len(prime_replacements) > max_family_size:
                        max_family_size = len(prime_replacements)
                        ans = prime_replacements
    print(ans, max_family_size)


def get_replacements(n: int, tup: tuple[int, ...]) -> set[int]:
    s = str(n)
    replacements = set()
    for i in range(10):
        for idx in tup:
            s = s[:idx] + str(i) + s[idx + 1 :]
        replacements.add(int(s))
    return replacements


if __name__ == "__main__":
    main()
