def main():
    s = ""
    for i in range(1, 1000001):
        s += str(i)
    print(int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999]) * int(s[999999]))


if __name__ == "__main__":
    main()
