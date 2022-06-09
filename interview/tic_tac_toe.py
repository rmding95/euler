class TicTacToe:
    def __init__(self, n: int):
        self.size = n
        self.grid: list[list[str]] = []
        for i in range(self.size):
            self.grid.append([""] * self.size)
        self.players: dict[int, str] = {1: "X", 2: "O"}
        self.right_diag: set[tuple[int, int]] = set()
        self.left_diag: set[tuple[int, int]] = set()
        for i in range(self.size):
            self.right_diag.add((i, i))
            self.left_diag.add((self.size - 1 - i, i))
        self.row_count: list[int] = [0] * self.size
        self.col_count: list[int] = [0] * self.size
        self.diag = 0
        self.anti_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        player_character = self.players[player]
        self.grid[row][col] = player_character
        # check up/down
        vertical_slice = [self.grid[i][col] for i in range(self.size)]
        if all([x == player_character for x in vertical_slice]):
            return player
        # check left/right
        if all([x == player_character for x in self.grid[row]]):
            return player
        if (row, col) in self.right_diag:
            right_diag_slice = [self.grid[i][i] for i in range(self.size)]
            if all([x == player_character for x in right_diag_slice]):
                return player
        if (row, col) in self.left_diag:
            left_diag_slice = [self.grid[self.size - 1 - i][i] for i in range(self.size)]
            if all([x == player_character for x in left_diag_slice]):
                return player
        return 0

    def move_optimized(self, row: int, col: int, player: int) -> int:
        self.grid[row][col] = self.players[player]
        current_player = 1 if player == 1 else -1
        self.row_count[row] += current_player
        self.col_count[col] += current_player
        if (row, col) in self.right_diag:
            self.diag += current_player
        if (row, col) in self.left_diag:
            self.anti_diag += current_player
        if (
            abs(self.row_count[row]) == self.size
            or abs(self.col_count[col]) == self.size
            or abs(self.diag) == self.size
            or abs(self.anti_diag) == self.size
        ):
            return player
        return 0


def main():
    tc = TicTacToe(2)
    print(tc.move_optimized(0, 0, 2))
    print(tc.move_optimized(1, 1, 1))
    print(tc.move_optimized(0, 1, 2))
    print(tc.grid)


if __name__ == "__main__":
    main()
