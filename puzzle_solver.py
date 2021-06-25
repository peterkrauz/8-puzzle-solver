from board import get_input_matrix, get_puzzle_board, assign_void_value_to_puzzle_board
from presenter import get_matrix_size, get_solution_type, exhibit_puzzle_board
from solution_type import SolutionType


def solve_puzzle():
    puzzle_board = build_puzzle_board()
    exhibit_puzzle_board(puzzle_board)

    puzzle_board = prepare_puzzle_board(puzzle_board)
    exhibit_puzzle_board(puzzle_board)

    solution_type = get_solution_type()
    puzzle_solver_function = get_puzzle_solver(solution_type)
    puzzle_solver_function()


def build_puzzle_board():
    matrix_size = get_matrix_size()
    puzzle_input = get_input_matrix(matrix_size)
    return get_puzzle_board(puzzle_input, matrix_size)


def prepare_puzzle_board(puzzle_board):
    return assign_void_value_to_puzzle_board(puzzle_board)


def get_puzzle_solver(solution_type):
    solution_options = SolutionType.options()
    _, solver = solution_options[solution_type]
    return solver


if __name__ == '__main__':
    solve_puzzle()
