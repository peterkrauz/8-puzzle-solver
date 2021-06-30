from random import shuffle

from movement import find_index_for_value
from presenter import get_user_void_square_choice, confirm_user_void_square_choice, prompt_user_for_tile_value, \
    warn_user_of_repeated_value, exhibit_puzzle_board


# def get_input_matrix(matrix_size):
#     return [cell for cell in range(1, (matrix_size ** 2) + 1)]


def get_puzzle_board(puzzle_input, matrix_size):
    puzzle_board = [[] for _ in range(int(len(puzzle_input) / matrix_size))]
    for index, item in enumerate(puzzle_input):
        puzzle_board[index % matrix_size].append(item)

    return puzzle_board


def build_puzzle_board(matrix_size):
    inserted_values = set()
    puzzle_board = [[] for _ in range(matrix_size)]
    value_limit = matrix_size ** 2

    while True:
        tile_value = prompt_user_for_tile_value()
        if tile_value in inserted_values:
            warn_user_of_repeated_value(value_limit)
            continue

        inserted_values.add(tile_value)
        row_index = (len(inserted_values) - 1) // matrix_size
        puzzle_board[row_index].append(tile_value)
        exhibit_puzzle_board(puzzle_board)

        if len(inserted_values) == value_limit:
            return puzzle_board


def assign_void_value_to_puzzle_board(puzzle_board):
    searching_for_void_square = True
    while searching_for_void_square:
        void_square_value = int(get_user_void_square_choice())
        user_choice = confirm_user_void_square_choice(void_square_value)

        if user_choice == 's':
            row, column = find_index_for_value(puzzle_board, void_square_value)
            puzzle_board[row][column] = None
            # test_board = [
            #     [None, 1, 3],
            #     [4, 2, 5],
            #     [7, 8, 6],
            # ]
            return puzzle_board, void_square_value
