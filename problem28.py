SPIRAL_SIZE = 1001


def main():
    sum = 0
    # upper right diagonal
    for i in range(3, SPIRAL_SIZE + 2, 2):
        sum += i * i
    # upper left diagonal
    for k, n in enumerate(range(3, SPIRAL_SIZE + 2, 2)):
        sum += (n * n) - (2 * (k + 1))
    # down left diagonal
    for k, n in enumerate(range(3, SPIRAL_SIZE + 2, 2)):
        sum += (n * n) - (4 * (k + 1))
    # down right diagonal
    for k, n in enumerate(range(1, SPIRAL_SIZE, 2)):
        sum += (n * n) + (2 * (k + 1))
    sum += 1
    print(sum)


if __name__ == "__main__":
    main()
