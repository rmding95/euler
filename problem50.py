from util import primes_up_to_n_optimized

LIMIT = 1000000


def main():
    primes = primes_up_to_n_optimized(LIMIT)
    print(primes)
    cache = set(primes)
    max_seq_len = 0
    max_prime = 0
    for i in range(LIMIT):
        cum_sum = 0
        seq_len = 0
        for prime in primes[i:]:
            cum_sum += prime
            if cum_sum > LIMIT:
                break
            seq_len += 1
            if cum_sum in cache and seq_len > max_seq_len:
                # print(f"inner {cum_sum} {seq_len}")
                max_seq_len = seq_len
                max_prime = cum_sum
    print(max_seq_len)
    print(max_prime)


if __name__ == "__main__":
    main()
