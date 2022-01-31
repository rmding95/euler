import time

GRID_SIZE = 20


def main():
    tic = time.time()
    print(dfs(GRID_SIZE))
    print(time.time() - tic)


def dfs(grid_size: int) -> int:
    print(_dfs_helper(grid_size, 0, 0, {}))


def _dfs_helper(size: int, row: int, col: int, cache: dict[tuple[int, int], int]) -> int:
    if row == size or col == size:
        return 1
    if (row, col) in cache:
        return cache[(row, col)]
    cache[(row, col)] = _dfs_helper(size, row + 1, col, cache) + _dfs_helper(size, row, col + 1, cache)
    return cache[(row, col)]


if __name__ == "__main__":
    main()
