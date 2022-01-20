NUM_TO_WORDS_MAP = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    1000: "onethousand",
    0: "",
}
# 999
# nine hundred and ninety nine


def main():
    total_len = 0
    for i in range(1, 1001):
        if i == 1000:
            word = NUM_TO_WORDS_MAP[i]
        elif i >= 100:
            hundreds_place = i // 100
            tens_word = get_tens_word(i % 100)
            word = f"{NUM_TO_WORDS_MAP[hundreds_place]}hundred"
            if len(tens_word) > 0:
                word += f"and{tens_word}"
        else:
            word = get_tens_word(i)
        print(word)
        total_len += len(word)
    print(total_len)


def get_tens_word(n: int) -> str:
    if n >= 21:
        tens_place = n // 10
        ones_place = n % 10
        word = f"{NUM_TO_WORDS_MAP[tens_place * 10]}{NUM_TO_WORDS_MAP[ones_place]}"
    else:
        word = NUM_TO_WORDS_MAP[n]
    return word


if __name__ == "__main__":
    main()
