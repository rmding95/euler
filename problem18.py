FILENAME = "euler/triangle.txt"


def main():
    triangle: list[list[int]] = []
    with open(FILENAME) as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            split = line.split(" ")
            triangle.append([int(x) for x in split])
    running_max = 0
    for row_idx, row in enumerate(triangle):
        if row_idx == 0:
            continue
        else:
            for col_idx, _ in enumerate(row):
                if col_idx == 0:
                    row[col_idx] += triangle[row_idx - 1][col_idx]
                elif col_idx == len(row) - 1:
                    row[col_idx] += triangle[row_idx - 1][col_idx - 1]
                else:
                    row[col_idx] += max(triangle[row_idx - 1][col_idx - 1], triangle[row_idx - 1][col_idx])
        running_max = max(running_max, max(row))
        # print(triangle)
    print(running_max)


if __name__ == "__main__":
    main()
