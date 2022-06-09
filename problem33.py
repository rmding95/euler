from util import get_digits, timer


@timer
def main():
    ans_num = 1
    ans_denom = 1
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            frac = numerator / denominator
            numerator_digits = get_digits(numerator)
            denominator_digits = get_digits(denominator)
            for num_idx, num_digit in enumerate(numerator_digits):
                for denom_idx, denom_digit in enumerate(denominator_digits):
                    if num_digit != 0 and denom_digit != 0 and num_digit == denom_digit:
                        num_d = 0 if num_idx == 1 else 1
                        denom_d = 0 if denom_idx == 1 else 1
                        if denominator_digits[denom_d] == 0:
                            continue
                        reduced_frac = numerator_digits[num_d] / denominator_digits[denom_d]
                        if reduced_frac == frac:
                            print(f"{numerator} / {denominator}")
                            print(f"{numerator_digits[num_d]} / {denominator_digits[denom_d]}\n")
                            ans_num *= numerator
                            ans_denom *= denominator
    print(f"{ans_num} / {ans_denom}")
    print(ans_num / ans_denom)


if __name__ == "__main__":
    main()
