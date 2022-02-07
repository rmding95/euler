from collections import defaultdict
from typing import DefaultDict, NamedTuple

COINS = [1, 2, 5]


class CoinCombination(NamedTuple):
    coin: int
    number: int

    def __repr__(self) -> str:
        return f"({self.coin}, {self.number})"


def main():
    cache: DefaultDict[int, list[list[CoinCombination]]] = defaultdict(list)
    for coin in COINS:
        print(coin, get_combinations(coin, cache))


def get_combinations(value: int, cache: DefaultDict[int, list[list[CoinCombination]]]) -> list[list[CoinCombination]]:
    _combination_helper(value, cache)
    return cache[value]


def _combination_helper(value: int, cache: DefaultDict[int, list[list[CoinCombination]]]) -> None:
    for coin in COINS:
        if coin >= value:
            # cache[value].append([CoinCombination(coin, 1)])
            return
        top_level_combination: list[CoinCombination] = []
        top_level_combination.append(CoinCombination(coin, value // coin))
        if value % coin != 0:
            top_level_combination.append(CoinCombination(1, value % coin))
        cache[value].append(top_level_combination)

        for combination in top_level_combination:
            if combination.coin == 1:
                continue
            for i in range(combination.number):
                for replacement_combinations in cache[combination.coin]:
                

if __name__ == "__main__":
    main()
