import time

from board import assign_void_value_to_puzzle_board, build_puzzle_board
from presenter import get_matrix_size, get_solution_type, exhibit_puzzle_board, warn_uniform_cost_slowness, \
    exhibit_search_info, prompt_for_path_exhibition, exhibit_search_path, prompt_for_hard_shuffle, \
    display_program_start, prompt_for_puzzle_board_reuse
from solution_type import SolutionType


def solve_puzzle():
    matrix_size = get_matrix_size()
    if matrix_size > 3:
        warn_uniform_cost_slowness()

    original_board = build_puzzle_board(matrix_size)

    puzzle_board, void_value = prepare_puzzle_board(original_board)
    exhibit_puzzle_board(puzzle_board)

    run_puzzle_solver(puzzle_board, void_value)

    reuse_board_choice = prompt_for_puzzle_board_reuse()
    while reuse_board_choice == 's':
        run_puzzle_solver(puzzle_board, void_value)
        reuse_board_choice = prompt_for_puzzle_board_reuse()


def run_puzzle_solver(puzzle_board, void_value):
    exhibit_puzzle_board(puzzle_board)

    solution_type = get_solution_type()
    solution_type, puzzle_solver_function = get_puzzle_solver(solution_type)

    execution_start = time.process_time()
    display_program_start()
    search_info = puzzle_solver_function(puzzle_board, void_value)
    exhibit_search_info(search_info, time.process_time() - execution_start, solution_type)

    path_exhibition_user_choice = prompt_for_path_exhibition()
    if path_exhibition_user_choice == 's':
        exhibit_search_path(search_info.path)


def prepare_puzzle_board(puzzle_board):
    return assign_void_value_to_puzzle_board(puzzle_board)


def get_puzzle_solver(solution_type):
    solution_options = SolutionType.options()
    name, solver = solution_options[solution_type]
    return name, solver


if __name__ == '__main__':
    solve_puzzle()
