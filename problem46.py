from util import primes_up_to_n_optimized


def main():
    primes = primes_up_to_n_optimized(int(1e6))
    cache = set(primes)
    for i in range(3, int(1e6), 2):
        if i in cache:
            continue
        squares = 1
        found = False
        while 2 * pow(squares, 2) + 2 < i:
            diff = i - 2 * pow(squares, 2)
            if diff in cache:
                # print(f"{i}: {diff} + 2*{squares}^2")
                found = True
                break
            squares += 1
        if not found:
            print(i)
            return


if __name__ == "__main__":
    main()
