def main():
    cache = {}
    max_len = 1
    max_start = 0
    for i in range(2, 1000001):
        i_len = collatz_sequence(i, cache)
        if i_len > max_len:
            max_len = i_len
            max_start = i
    print(max_start, max_len)


def collatz_sequence(start: int, cache: dict[int, int]) -> int:
    """Returns the length of the collatz sequence beginning at start"""
    n = start
    seq_len = 0
    curr_seq = []
    while n > 0:
        if n in cache:
            seq_len += cache[n]
            break
        curr_seq.append(n)
        if n == 1:
            n = -1
        elif n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        seq_len += 1
    for idx, val in enumerate(curr_seq):
        if val not in cache:
            cache[val] = seq_len - idx
    return seq_len


if __name__ == "__main__":
    main()
