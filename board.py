from random import shuffle

from movement import find_index_for_value
from presenter import get_user_void_square_choice, confirm_user_void_square_choice


def get_input_matrix(matrix_size, hard_shuffle):
    puzzle_input = [cell for cell in range(1, (matrix_size ** 2) + 1)]
    if hard_shuffle:
        shuffle(puzzle_input)
    return puzzle_input


def get_puzzle_board(puzzle_input, matrix_size, hard_shuffle):
    puzzle_board = [[] for _ in range(int(len(puzzle_input) / matrix_size))]
    for index, item in enumerate(puzzle_input):
        puzzle_board[index % matrix_size].append(item)

    if not hard_shuffle:
        shuffle(puzzle_board)
    return puzzle_board


def assign_void_value_to_puzzle_board(puzzle_board):
    searching_for_void_square = True
    while searching_for_void_square:
        void_square_value = int(get_user_void_square_choice())
        user_choice = confirm_user_void_square_choice(void_square_value)

        if user_choice == 's':
            row, column = find_index_for_value(puzzle_board, void_square_value)
            puzzle_board[row][column] = None
            return puzzle_board, void_square_value
