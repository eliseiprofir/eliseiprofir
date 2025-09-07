from random import randrange


def display_board(board: list[list[str | int]]) -> None:
    board_view: str = "+-------+-------+-------+\n"
    for row in board:
        board_view += "|       |       |       |\n"
        for column in row:
            board_view += f"|   {column}   "
        board_view += "|\n"
        board_view += "|       |       |       |\n"
        board_view += "+-------+-------+-------+\n"
    board_view = board_view.rstrip('\n')
    print(board_view)


def valid_choice(user_input: str, free_positions: list[int]) -> bool:
    if not user_input.isdigit():
        print("Bad move (enter a number) - repeat your input!")
        return False
    elif int(user_input) > 9 or int(user_input) < 1:
        print("Bad move (enter a number between 1-9) - repeat your input!")
        return False
    elif int(user_input) not in free_positions:
        print("Field already occupied - repeat your input!")
        return False
    return True


def user_move(board: list[list[str | int]]) -> None:
    free_fields: list[tuple[int, int]] = make_list_of_free_fields(board)
    free_positions: list[int] = [board[row][column] for row, column in free_fields]
    while True:
        move: str = input("Enter your move: ")
        if valid_choice(move, free_positions):
            move: int = int(move)
            for row, column in free_fields:
                if board[row][column] == move:
                    board[row][column] = 'X'
        break


def computer_move(board: list[list[str | int]]) -> None:
    free_fields: list[tuple[int, int]] = make_list_of_free_fields(board)
    count_free_fields: int = len(free_fields)
    if count_free_fields > 0:
        move: int = randrange(count_free_fields)
        row, column = free_fields[move]
        board[row][column] = '0'


def make_list_of_free_fields(board: list[list[str | int]]) -> list[[tuple[int, int]]]:
    free_fields: list[tuple[int, int]] = []
    for row in range(3):
        for column in range(3):
            if board[row][column] not in ['0', 'X']:
                free_fields.append((row, column))
    return free_fields


def victory_for(board: list[list[str | int]], sign: str) -> bool:
    for row, row_c in enumerate(board):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True
        for column, column_c in enumerate(row_c):
            if board[0][column] == board[1][column] == board[2][column] == sign:
                return True
            if (board[0][0] == board[1][1] == board[2][2] == sign) \
                    or (board[0][2] == board[1][1] == board[2][0] == sign):
                return True
    return False


def main() -> None:
    board: list[list[int | str]] = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
    free_fields: list[tuple[int, int]] = make_list_of_free_fields(board)
    print(free_fields)
    human_turn: bool = True
    while True:
        display_board(board)
        if human_turn:
            user_move(board)
            victory: bool = victory_for(board, 'X')
        else:
            computer_move(board)
            victory: bool = victory_for(board, '0')
        if victory or free_fields == []:
            break
        human_turn = not human_turn
        free_fields = make_list_of_free_fields(board)

    display_board(board)
    if victory_for(board, '0'):
        print('I won!')
    elif victory_for(board, 'X'):
        print('You won!')
    else:
        print('Tie!')


if __name__ == "__main__":
    main()
