from solvers.search_info import SearchInfo


def solve_puzzle(puzzle_board, void_value) -> SearchInfo:
    print('A* Precise')
    # h1(n) = number of misplaced tiles from current state to target state
    # h2(n) = number of misplaced tiles from initial state to current state
