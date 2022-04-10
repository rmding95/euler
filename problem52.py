from collections import defaultdict

LIMIT = 5


def main():
    power_of_ten = 4
    # while True:
    #     num = pow(10, power_of_ten)
    #     if num * 6 > pow(10, power_of_ten + 1):
    #         power_of_ten += 1
    #         continue
    while True:
        num = pow(10, power_of_ten)
        while num * 6 < pow(10, power_of_ten + 1):
            digits = defaultdict(int)
            found = True
            n_copy = num
            while n_copy > 0:
                digits[n_copy % 10] += 1
                n_copy //= 10
            for idx, val in enumerate([2]):
                multiple = num * val
                while multiple > 0:
                    digits[multiple % 10] += 1
                    multiple //= 10
                if not all([x == idx + 1 for x in digits.values()]):
                    found = False
                    break
            if found:
                print(num)
                return
            num += 1
        power_of_ten += 1


if __name__ == "__main__":
    main()
