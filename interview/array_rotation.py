def main():
    print(shift_list_by_n([1, 2, 3], 1))
    print(shift_list_by_n([1, 2, 3, 4, 5], 3))


def shift_list_by_n(input: list[int], n: int) -> list[int]:
    current_idx = 0
    current_num = input[current_idx]
    for _ in range(0, len(input)):
        next_idx = (current_idx + n) % len(input)
        next_num = input[next_idx]
        input[next_idx] = current_num
        current_num = next_num
        current_idx = next_idx
    return input


if __name__ == "__main__":
    main()
