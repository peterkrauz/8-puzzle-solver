def solve_puzzle(puzzle_board):
    print('A* Precise')
    # h1(n) = number of misplaced tiles from current state to target state
    # h2(n) = number of misplaced tiles from initial state to current state
