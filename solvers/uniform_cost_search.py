from movement import get_next_moves_for_board, add_moves_to_frontier_boards, board_is_solution
from solvers.node import Node
from solvers.search_info import build_search_info


def solve_puzzle(puzzle_board, void_value):
    frontier_puzzle_boards = set()
    nodes_to_visit = [Node(puzzle_board, parent_node=None)]

    visited_nodes = []
    expanded_nodes = 0
    largest_frontier_size = 0

    while True:
        current_node = nodes_to_visit.pop(0)

        if board_is_solution(current_node.puzzle_board, void_value):
            return build_search_info(visited_nodes, expanded_nodes, largest_frontier_size, current_node)

        child_nodes_boards = get_next_moves_for_board(current_node.puzzle_board, frontier_puzzle_boards)
        frontier_puzzle_boards = add_moves_to_frontier_boards(child_nodes_boards, frontier_puzzle_boards)

        for child_board in child_nodes_boards:
            nodes_to_visit.append(Node(child_board, current_node))

        visited_nodes.append(current_node)
        expanded_nodes += len(child_nodes_boards)
        current_frontier_size = len(nodes_to_visit)
        if current_frontier_size > largest_frontier_size:
            largest_frontier_size = current_frontier_size
