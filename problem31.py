from util import timer

COINS = [200, 100, 50, 20, 10, 5, 2, 1]


@timer
def main():
    print(dfs())


def dfs() -> int:
    return _dfs_helper(200, 0, {})


def _dfs_helper(amount: int, coin_index: int, cache: dict[tuple[int, int], int]) -> int:
    if (amount, coin_index) in cache:
        return cache[amount, coin_index]
    coin_amount = COINS[coin_index]
    if coin_amount == 1:
        return 1
    combinations = 0
    i = 0
    while i * coin_amount <= amount:
        combinations += _dfs_helper(amount - i * coin_amount, coin_index + 1, cache)
        i += 1
    cache[(amount, coin_index)] = combinations
    return combinations


if __name__ == "__main__":
    main()
