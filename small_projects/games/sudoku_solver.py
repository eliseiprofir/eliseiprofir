class Board:
    def __init__(self, board: list[list[int]]) -> None:
        self.board: list[list[int]] = board

    def __str__(self) -> str:
        board_str: str = ''
        for row in self.board:
            row_str: list[str] = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str

    def find_empty_cell(self) -> tuple[int, int] | None:
        for row, contents in enumerate(self.board):
            try:
                col: int = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row: int, num: int) -> bool:
        return num not in self.board[row]

    def valid_in_col(self, col: int, num: int) -> bool:
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row: int, col: int, num: int) -> bool:
        row_start: int = (row // 3) * 3
        col_start: int = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty: tuple[int, int], num: int) -> bool:
        row, col = empty
        valid_in_row: bool = self.valid_in_row(row, num)
        valid_in_col: bool = self.valid_in_col(col, num)
        valid_in_square: bool = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self) -> bool:
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False


def solve_sudoku(board: list[list[int]]) -> Board:
    gameboard: Board = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard


puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]


if __name__ == "__main__":
    solve_sudoku(puzzle)
