def main():
    print(last_digit_mersenne_prime(6972593))
    print(last_digit_mersenne_prime(7))
    print(last_digit_mersenne_prime(13))


def last_digit_mersenne_prime(n: int) -> int:
    """Calculate the last digit of a mersenne prime of the form 2^n-1"""
    powers_of_two_cycle = [2, 4, 8, 6]
    digit = powers_of_two_cycle[(n % 4) - 1]
    return digit - 1


if __name__ == "__main__":
    main()
