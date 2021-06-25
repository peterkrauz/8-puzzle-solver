from solvers.a_star_strong_search import solve_puzzle as a_star_strong_solution
from solvers.a_star_search_weak_search import solve_puzzle as a_star_weak_solution
from solvers.uniform_cost_search import solve_puzzle as uniform_cost_solution


class SolutionType:
    UNIFORM_COST = 1, 'Custo uniforme', uniform_cost_solution
    A_STAR_WEAK = 2, 'A* com heurística simples', a_star_weak_solution
    A_STAR_STRONG = 3, 'A* com heurística precisa', a_star_strong_solution

    @classmethod
    def options(cls):
        solutions = [
            cls.UNIFORM_COST,
            cls.A_STAR_WEAK,
            cls.A_STAR_STRONG
        ]
        return {
            index: (text, function)
            for index, text, function in solutions
        }
