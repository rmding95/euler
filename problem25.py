from itertools import permutations

LIMIT = 10


def main():
    itr = permutations(range(LIMIT), LIMIT)
    counter = 1
    for v in itr:
        if counter == 1000000:
            print(v)
            break
        counter += 1


if __name__ == "__main__":
    main()
