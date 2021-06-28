from solvers.node import Node


def compute_simple_heuristic_value_for_node(node: Node, void_square_value: int) -> int:
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


def compute_node_index(heuristic_value: int, nodes_to_visit, void_square_value: int, default_index: int) -> int:
    for index, node in enumerate(nodes_to_visit):
        if heuristic_value < compute_simple_heuristic_value_for_node(node, void_square_value):
            if index == 0:
                return index
            else:
                return index - 1

    return default_index
