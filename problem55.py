from util import timer

MAX_ITERATIONS = 50
LIMIT = 100000


@timer
def main():
    count = 0
    nums = set()
    for i in range(1, LIMIT):
        if is_lychrel_num(i):
            count += 1
            nums.add(i)
    print(count)
    # print(nums)


def is_lychrel_num(n: int) -> bool:
    itrs = 0
    n_itr = n
    palindrome_cache = set()
    reverse_num_cache: dict[int, int] = {}
    while itrs < MAX_ITERATIONS:
        if n_itr in reverse_num_cache:
            rev = reverse_num_cache[n_itr]
        else:
            rev = reverse_num(n_itr)
            reverse_num_cache[n_itr] = rev
        n_itr = n_itr + rev
        if n_itr in palindrome_cache or is_palindrome(n_itr):
            palindrome_cache.add(n_itr)
            return False
        itrs += 1
    return True


def reverse_num(n: int) -> int:
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


def is_palindrome(n: int) -> bool:
    s = str(n)
    for idx, _ in enumerate(s[: len(s) // 2]):
        if s[idx] != s[-(idx + 1)]:
            return False
    return True


if __name__ == "__main__":
    main()
