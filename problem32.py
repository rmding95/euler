from util import timer

digits_cache = {}


@timer
def main():
    seen: set[int] = set()
    digit_cache: dict[int, int] = {}
    ans = 0
    for i in range(1, 10000):
        for j in range(1, 1000):
            prod = i * j
            digit_count = count_digits(i, digit_cache) + count_digits(j, digit_cache) + count_digits(prod, digit_cache)
            if digit_count != 9:
                continue
            if prod not in seen and is_one_to_nine_pandigital(i, j):
                seen.add(prod)
                ans += prod
                print(f"{i} * {j} = {prod}")
    print(ans)


def is_one_to_nine_pandigital(a: int, b: int) -> bool:
    prod = a * b
    digits: set[int] = set()
    expected: set[int] = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    extract_digits(digits, a, b, prod)
    return expected == digits


def is_one_to_nine_pandigital_binary(a: int, b: int) -> bool:
    result = 0
    prod = a * b
    concat = int(str(a) + str(b) + str(prod))
    while concat > 0:
        digit = concat % 10
        if digit == 0:
            return False
        result |= 1 << (concat - 1)
        concat //= 10
    return result == 0x1FF


def extract_digits(output: set[int], *args: int) -> None:
    global digits_cache
    for n in args:
        tmp: set[int] = set()
        if n in digits_cache:
            output.update(digits_cache[n])
        else:
            while n > 0:
                tmp.add(n % 10)
                output.add(n % 10)
                n //= 10
            digits_cache[n] = tmp
            output.update(tmp)


def count_digits(n: int, digit_cache: dict[int, int]) -> int:
    if n in digit_cache:
        return digit_cache[n]
    count = 0
    while n > 0:
        n //= 10
        count += 1
    digit_cache[n] = count
    return count


if __name__ == "__main__":
    main()
