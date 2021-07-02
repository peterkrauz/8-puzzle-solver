from movement import find_index_for_value


def compute_simple_heuristic_value_for_node(node, void_square_value):
    """
    Computes the number of misplaced tiles of a given puzzle board.
    Smaller values indicate better optimal paths.
    """
    heuristic_value = 0
    initial_value = 2 if void_square_value == 1 else 1

    for row in node.puzzle_board:
        for column in row:
            if column != initial_value:
                heuristic_value += 1
            initial_value += 1

    return heuristic_value


def compute_simple_heuristic_node_index(heuristic_value, nodes_to_visit, void_square_value, default_index):
    for index, node in enumerate(nodes_to_visit):
        if heuristic_value < compute_simple_heuristic_value_for_node(node, void_square_value):
            if index == 0:
                return index
            else:
                return index - 1

    return default_index


def compute_precise_heuristic_value_for_node(node, void_square_value):
    """
    Computes the sum of all manhattan distances between each tile
    and their desired position.
    """
    heuristic_value = 0
    initial_value = 2 if void_square_value == 1 else 1
    first_tile_value = initial_value

    target_board = build_ideal_board(initial_value, len(node.puzzle_board), void_square_value)

    for row_index, row in enumerate(node.puzzle_board):
        for column_index, column in enumerate(row):
            if target_board[row_index][column_index] != column:
                heuristic_value += compute_manhattan_distance_for_value(
                    column,
                    node.puzzle_board,
                    first_tile_value,
                    void_square_value
                )

    return heuristic_value


def compute_manhattan_distance_for_value(value, current_board, initial_value, void_square_value):
    matrix_size = len(current_board)
    target_board = build_ideal_board(initial_value, matrix_size, void_square_value)

    target_y, target_x = find_index_for_value(target_board, value)
    current_y, current_x = find_index_for_value(current_board, value)

    absolute_y = abs(current_y - target_y)
    absolute_x = abs(current_x - target_x)
    return absolute_y + absolute_x


def compute_precise_heuristic_node_index(heuristic_value, nodes_to_visit, void_square_value, default_index):
    for index, node in enumerate(nodes_to_visit):
        if heuristic_value < compute_precise_heuristic_value_for_node(node, void_square_value):
            if index == 0:
                return index
            else:
                return index - 1

    return default_index


def build_ideal_board(value, matrix_size, void_square_value):
    value -= 1
    ideal_board = [[] for _ in range(matrix_size)]
    for row in range(matrix_size):
        for _ in range(matrix_size):
            value += 1

            if value == void_square_value:
                value += 1

            if value == (matrix_size ** 2) + 1:
                value = None

            ideal_board[row].append(value)

    return ideal_board
