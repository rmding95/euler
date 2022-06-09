from collections import defaultdict
from typing import DefaultDict, Optional

FILENAME = "p096_sudoku.txt"
TEST_FILE = "test_sudoku.txt"


class SudokuSolver:
    def __init__(self):
        self.size = 9
        self.grid: list[list[int]] = []
        self.boxes: DefaultDict[int, set[int]] = defaultdict(set)
        self.rows: DefaultDict[int, set[int]] = defaultdict(set)
        self.cols: DefaultDict[int, set[int]] = defaultdict(set)
        self.solved = False

    def add_row(self, text: str, row_num: int) -> None:
        text = text.strip("\n")
        row: list[int] = []
        for col_idx, val in enumerate(text):
            if val == "0":
                row.append(0)
                continue
            int_val = int(val)
            row.append(int_val)
            box_num = self.get_box(row_num, col_idx)
            self.boxes[box_num].add(int_val)
            self.rows[row_num].add(int_val)
            self.cols[col_idx].add(int_val)
        self.grid.append(row)

    def get_box(self, row: int, col: int) -> int:
        """Returns the sub-box the (row, col) value is located in. Starts at 0 in the top left"""
        return (row // 3) * 3 + (col // 3)

    def solve(self) -> None:
        if self._backtrack():
            print(self.print_grid())
        else:
            print("no solution")

    def _backtrack(self) -> bool:
        next_square = self.find_empty_square()
        if not next_square:
            return True
        row, col = next_square
        for i in range(1, self.size + 1):
            if not self.can_place(i, row, col):
                continue
            self.place_value(i, row, col)
            if self._backtrack():
                return True
            self.remove_value(i, row, col)
        return False

    def can_place(self, val: int, row: int, col: int) -> bool:
        if self.grid[row][col] != 0:
            return False
        box = self.get_box(row, col)
        if val in self.boxes[box] or val in self.rows[row] or val in self.cols[col]:
            return False
        return True

    def place_value(self, val: int, row: int, col: int) -> None:
        self.grid[row][col] = val
        self.boxes[self.get_box(row, col)].add(val)
        self.rows[row].add(val)
        self.cols[col].add(val)

    def remove_value(self, val: int, row: int, col: int) -> None:
        self.grid[row][col] = 0
        self.boxes[self.get_box(row, col)].remove(val)
        self.rows[row].remove(val)
        self.cols[col].remove(val)

    def find_empty_square(self) -> Optional[tuple[int, int]]:
        for row_idx, row_val in enumerate(self.grid):
            for col_idx, col_val in enumerate(row_val):
                if col_val == 0:
                    return row_idx, col_idx
        return None

    def print_grid(self) -> str:
        s = ""
        for row in self.grid:
            for val in row:
                s += f"{val} "
            s += "\n"
        return s

    def __str__(self) -> str:
        return self.print_grid()


def main():
    ans = 0
    with open(FILENAME) as f:
        text = f.readlines()
        solver = SudokuSolver()
        row_counter = 0
        for line in text:
            if "Grid" in line:
                row_counter = 0
                solver = SudokuSolver()
                continue
            solver.add_row(line, row_counter)
            row_counter += 1
            if row_counter == 9:
                solver.solve()
                ans += solver.grid[0][0] * 100 + solver.grid[0][1] * 10 + solver.grid[0][2]
    print(ans)


if __name__ == "__main__":
    main()
