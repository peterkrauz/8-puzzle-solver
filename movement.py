from copy import deepcopy
from itertools import chain

from solvers.node import Node


class TileDirection:
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


def get_next_moves_for_board(puzzle_board: list[list], frontier_puzzle_boards: set[tuple]) -> list:
    matrix_size = len(puzzle_board) - 1
    y, x = find_index_for_value(puzzle_board, value=None)

    can_move_northward = y >= 1
    can_move_westward = x >= 1

    can_move_southward = y < matrix_size
    can_move_eastward = x < matrix_size

    next_moves = list()

    if can_move_northward:
        built_board = build_board_for_move_direction(puzzle_board, TileDirection.NORTH)
        if board_can_be_visited(built_board, frontier_puzzle_boards):
            next_moves.append(built_board)

    if can_move_westward:
        built_board = build_board_for_move_direction(puzzle_board, TileDirection.WEST)
        if board_can_be_visited(built_board, frontier_puzzle_boards):
            next_moves.append(built_board)

    if can_move_southward:
        built_board = build_board_for_move_direction(puzzle_board, TileDirection.SOUTH)
        if board_can_be_visited(built_board, frontier_puzzle_boards):
            next_moves.append(built_board)

    if can_move_eastward:
        built_board = build_board_for_move_direction(puzzle_board, TileDirection.EAST)
        if board_can_be_visited(built_board, frontier_puzzle_boards):
            next_moves.append(built_board)

    return next_moves


def get_child_nodes_for_node(node: Node, visited_nodes: list[Node]) -> list[Node]:
    matrix_size = len(node.puzzle_board) - 1
    void_square_coordinates = find_index_for_value(node.puzzle_board, value=None)
    void_square_y, void_square_x = void_square_coordinates

    can_move_northward = void_square_y >= 1
    can_move_westward = void_square_x >= 1

    can_move_southward = void_square_y < matrix_size
    can_move_eastward = void_square_x < matrix_size

    next_moves = list()
    visited_boards = [node.puzzle_board for node in visited_nodes]

    if can_move_northward:
        built_board = build_board_for_move_direction(node.puzzle_board, TileDirection.NORTH)
        if built_board not in visited_boards:
            next_moves.append(Node(built_board, parent_node=node))

    if can_move_westward:
        built_board = build_board_for_move_direction(node.puzzle_board, TileDirection.WEST)
        if built_board not in visited_boards:
            next_moves.append(Node(built_board, parent_node=node))

    if can_move_southward:
        built_board = build_board_for_move_direction(node.puzzle_board, TileDirection.SOUTH)
        if built_board not in visited_boards:
            next_moves.append(Node(built_board, parent_node=node))

    if can_move_eastward:
        built_board = build_board_for_move_direction(node.puzzle_board, TileDirection.EAST)
        if built_board not in visited_boards:
            next_moves.append(Node(built_board, parent_node=node))

    return next_moves


def board_can_be_visited(board: list[list], frontier_puzzle_boards: set[tuple]) -> bool:
    tuple_board = create_tuple_from_board(board)
    return tuple_board not in frontier_puzzle_boards


def create_tuple_from_board(board: list[list]) -> tuple:
    return tuple(list(chain.from_iterable(board)))


def build_board_for_move_direction(puzzle_board: list[list], tile_direction: int) -> list[list]:
    new_board = deepcopy(puzzle_board)
    void_square_y, void_square_x = find_index_for_value(new_board, value=None)

    if tile_direction == TileDirection.NORTH:
        switch_index = void_square_y - 1, void_square_x
        square_to_switch = new_board[void_square_y - 1][void_square_x]

    elif tile_direction == TileDirection.SOUTH:
        switch_index = void_square_y + 1, void_square_x
        square_to_switch = new_board[void_square_y + 1][void_square_x]

    elif tile_direction == TileDirection.EAST:
        switch_index = void_square_y, void_square_x + 1
        square_to_switch = new_board[void_square_y][void_square_x + 1]

    else:
        switch_index = void_square_y, void_square_x - 1
        square_to_switch = new_board[void_square_y][void_square_x - 1]

    new_board[void_square_y][void_square_x] = square_to_switch
    new_board[switch_index[0]][switch_index[1]] = None
    return new_board


def find_index_for_value(puzzle_board: list[list], value) -> tuple:
    row_index = 0
    for row in puzzle_board:
        column_index = 0
        for column in row:
            if column == value:
                return row_index, column_index
            column_index += 1
        row_index += 1


def add_moves_to_frontier_boards(new_boards: list[list], frontier_puzzle_boards: set[tuple]) -> set[tuple]:
    new_frontier_puzzle_boards = deepcopy(frontier_puzzle_boards)
    for board in new_boards:
        board_tuple = create_tuple_from_board(board)
        new_frontier_puzzle_boards.add(board_tuple)

    return new_frontier_puzzle_boards


def board_is_solution(puzzle_board: list[list], void_value) -> bool:
    stumbled_on_void_value = False

    if puzzle_board[0][0] not in [1, 2]:
        return False

    value = puzzle_board[0][0]
    # if puzzle_board[0][0] == 2:
    #     value = 2

    matrix_size = len(puzzle_board) - 1
    if puzzle_board[matrix_size][matrix_size] is not None:
        return False

    for row in puzzle_board:
        for column in row:
            if column and column != value:
                if column in range(void_value - 1, void_value + 2) and not stumbled_on_void_value:
                    stumbled_on_void_value = True
                else:
                    return False
            value += 1

    return True
