LIMIT = 1000000


def main():
    ans = 0
    for i in range(LIMIT):
        if is_palindrome(str(i)) and is_palindrome(f"{i:b}"):
            ans += i
    print(ans)


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


if __name__ == "__main__":
    main()
