from collections import defaultdict


def main():
    characters = []
    d = defaultdict(int)
    with open("p059_cipher.txt") as f:
        text = f.read()
        characters = text.split(",")
    for c in characters:
        d[int(c)] += 1
    print(len(d.keys()))


if __name__ == "__main__":
    main()
