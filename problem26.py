LIMIT = 10000


def main():
    max_cycle_len = 0
    max_i = 0
    for i in range(2, LIMIT):
        fraction, cycle_len = find_unit_fractional_cycles(i)
        if cycle_len > max_cycle_len:
            max_cycle_len = cycle_len
            max_i = i
    print(f"{max_i} has a {max_cycle_len} digit recurring cycle")


def find_unit_fractional_cycles(n: int) -> tuple[str, int]:
    dividend = 1
    fraction = ""
    remainders = ""
    cache = set()
    while True:
        remainder = (dividend * 10) % n
        quotient = dividend * 10 // n
        if (quotient, remainder) not in cache:
            cache.add((quotient, remainder))
        else:
            return (fraction, len(fraction))
        fraction += str(quotient)
        remainders += str(remainder)
        dividend = remainder
        if remainder == 0:
            break
    return (fraction, len(fraction))


if __name__ == "__main__":
    main()
