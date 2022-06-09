from typing import Optional

from util import get_digits

PANDIGITAL_SET = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
LIMIT = 10000


def main():
    ans = 0
    for i in range(1, LIMIT):
        tup = concat_pandigital_product(i)
        if not tup:
            continue
        n, pandigital_num = tup[0], tup[1]
        print(f"{i}: n: {n}, pandigital: {pandigital_num}")
        ans = max(ans, pandigital_num)
    print(ans)


def concat_pandigital_product(num: int) -> Optional[tuple[int, int]]:
    n_digits: set[int] = set()
    n = 1
    pandigital_num = ""
    while not n_digits == PANDIGITAL_SET:
        product = num * n
        pandigital_num += str(product)
        if len(pandigital_num) > 9:
            return None
        p_digits = set(get_digits(product))
        if not p_digits.isdisjoint(n_digits):
            return None
        n_digits.update(p_digits)
        n += 1
    return n - 1, int(pandigital_num)


if __name__ == "__main__":
    main()
