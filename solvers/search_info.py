from solvers.node import Node


class SearchInfo:

    def __init__(
            self,
            visited_nodes: int,
            expanded_nodes: int,
            largest_frontier_size: int,
            path: list[Node]
    ):
        self.visited_nodes = visited_nodes
        self.expanded_nodes = expanded_nodes
        self.largest_frontier_size = largest_frontier_size
        self.path = path


def get_path_for_node(node: Node) -> list[Node]:
    path = []
    node_to_search = node

    while node_to_search.parent_node is not None:
        path.append(node_to_search)
        node_to_search = node_to_search.parent_node

    return list(reversed(path))
