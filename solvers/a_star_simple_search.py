from movement import board_is_solution, get_child_nodes_for_node
from solvers.heuristics import compute_simple_heuristic_value_for_node, compute_node_index
from solvers.node import Node
from solvers.search_info import SearchInfo, build_search_info


def solve_puzzle(puzzle_board, void_value) -> SearchInfo:
    nodes_to_visit = [Node(puzzle_board, parent_node=None)]

    visited_nodes = []
    expanded_nodes = 1
    largest_frontier_size = 1

    while True:
        current_node = nodes_to_visit.pop(0)

        if board_is_solution(current_node.puzzle_board, void_value):
            return build_search_info(visited_nodes, expanded_nodes, largest_frontier_size, current_node)

        child_nodes_from_current_node = get_child_nodes_for_node(current_node, visited_nodes)

        for child_node in child_nodes_from_current_node:
            heuristic_value = compute_simple_heuristic_value_for_node(child_node, void_value)
            index = compute_node_index(heuristic_value, nodes_to_visit, void_value, len(nodes_to_visit) - 1)
            nodes_to_visit.insert(index, child_node)

        visited_nodes.append(current_node)
        expanded_nodes += len(child_nodes_from_current_node)
        current_frontier_size = len(nodes_to_visit)
        if current_frontier_size > largest_frontier_size:
            largest_frontier_size = current_frontier_size
