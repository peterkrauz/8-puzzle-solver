from solvers.a_star_precise_search import solve_puzzle as a_star_precise_solution
from solvers.a_star_simple_search import solve_puzzle as a_star_simple_solution
from solvers.uniform_cost_search import solve_puzzle as uniform_cost_solution


class SolutionType:
    UNIFORM_COST = 1, 'Custo uniforme', uniform_cost_solution
    A_STAR_SIMPLE = 2, 'A* com heurística simples', a_star_simple_solution
    A_STAR_PRECISE = 3, 'A* com heurística precisa', a_star_precise_solution

    @classmethod
    def options(cls):
        solutions = [
            cls.UNIFORM_COST,
            cls.A_STAR_SIMPLE,
            cls.A_STAR_PRECISE
        ]
        return {
            index: (text, function)
            for index, text, function in solutions
        }
