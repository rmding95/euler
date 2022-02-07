POWER = 1000


def main():
    sum = 0
    for i in range(1, POWER + 1):
        sum += pow(i, i, int(1e10))
    print(sum % int(1e10))


if __name__ == "__main__":
    main()
