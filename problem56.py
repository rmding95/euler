from util import get_digits


def main():
    ans = 0
    ans_tup = ()
    for i in range(90, 100):
        for j in range(90, 100):
            n = pow(i, j)
            digits = get_digits(n)
            digit_sum = sum(digits)
            if sum(digits) > ans:
                ans = digit_sum
                ans_tup = (i, j)
    print(ans)
    print(ans_tup)


if __name__ == "__main__":
    main()
