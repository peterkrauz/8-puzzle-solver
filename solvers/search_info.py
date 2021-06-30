from solvers.node import Node


class SearchInfo:

    def __init__(
            self,
            visited_nodes: int,
            expanded_nodes: int,
            largest_frontier_size: int,
            path: list
    ):
        self.visited_nodes = visited_nodes
        self.expanded_nodes = expanded_nodes
        self.largest_frontier_size = largest_frontier_size
        self.path = path


def build_search_info(
        visited_nodes: list,
        expanded_nodes: int,
        largest_frontier_size: int,
        solution_node
) -> SearchInfo:
    return SearchInfo(
        visited_nodes=len(visited_nodes),
        expanded_nodes=expanded_nodes,
        largest_frontier_size=largest_frontier_size,
        path=get_path_for_node(solution_node)
    )


def get_path_for_node(node) -> list:
    path = []
    node_to_search = node

    while node_to_search.parent_node is not None:
        path.append(node_to_search)
        node_to_search = node_to_search.parent_node

    path.append(node_to_search)

    return list(reversed(path))
