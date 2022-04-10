from math import ceil, factorial

N_LIMIT = 100
LIMIT = 1000000


def main():
    factorial_cache: dict[int, int] = {}
    total = 0
    # for i in range(0, 22):
    #     print(num_combinations(21, i, factorial_cache))
    for i in range(1, N_LIMIT + 1):
        f_val = get_factorial(i, factorial_cache)
        if f_val < LIMIT:
            continue
        num_total = 0
        for j in range(ceil(i / 2) + 1, i):
            val = num_combinations(i, j, factorial_cache)
            if val > LIMIT:
                num_total += 1
            else:
                if num_total > 0:
                    num_total *= 2
                    if i % 2 == 0:
                        num_total += 1
                    else:
                        num_total += 2
                break
        total += num_total
    print(total)


def get_factorial(n: int, factorial_cache: dict[int, int]) -> int:
    if n in factorial_cache:
        return factorial_cache[n]
    else:
        val = factorial(n)
        factorial_cache[n] = val
        return val


def num_combinations(n: int, r: int, factorial_cache: dict[int, int]) -> int:
    assert r <= n
    return get_factorial(n, factorial_cache) // (
        get_factorial(r, factorial_cache) * get_factorial(n - r, factorial_cache)
    )


if __name__ == "__main__":
    main()
