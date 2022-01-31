POWER = 5


def main():
    nums: list[int] = []
    for i in range(2, 1000000):
        num = i
        digit_sum = 0
        while num > 0:
            digit = num % 10
            digit_sum += pow(digit, POWER)
            num //= 10
        if digit_sum == i:
            nums.append(i)
    print(nums)
    print(sum(nums))


if __name__ == "__main__":
    main()
