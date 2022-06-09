from itertools import permutations

from util import is_prime, timer


@timer
def main():
    n = 7
    for p in permutations(range(n, 0, -1), n):
        if p[n - 1] % 2 == 0 or p[n - 1] % 5 == 0:
            continue
        num = 0
        for i in range(n):
            num += pow(10, n - i - 1) * p[i]
        if is_prime(num):
            print(f"{num} is prime")
            break


if __name__ == "__main__":
    main()
