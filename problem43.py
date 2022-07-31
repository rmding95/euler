from itertools import permutations

from util import tuple_to_int

DIVISORS = (2, 3, 5, 7, 11, 13, 17)
SUB_STR_LEN = 3


def main():
    ans = 0
    for p in permutations(range(10), 10):
        if p[0] == 0:
            continue
        valid = True
        for i in range(1, len(p) - SUB_STR_LEN + 1):
            sub_str = p[i] * 100 + p[i + 1] * 10 + p[i + 2]
            if sub_str % DIVISORS[i - 1] != 0:
                valid = False
                break
        if valid:
            num = tuple_to_int(p)
            ans += num
    print(ans)


if __name__ == "__main__":
    main()
