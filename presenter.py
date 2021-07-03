import time

from solution_type import SolutionType
from solvers.node import Node
from solvers.search_info import SearchInfo


class CliFormatter:
    UNDERLINE = '\033[4m'
    HEADER = '\033[95m'
    BOLD = '\033[1m'

    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

    END = '\033[0m'


def get_matrix_size():
    matrix_size = int(input('Qual o tamanho desejado para o lado do tabuleiro?'))
    return matrix_size


def get_solution_type():
    print('\nDeseja rodar a busca em qual dos seguintes modos?')
    solution_prompt = ''
    for option_index, (option_text, _) in SolutionType.options().items():
        solution_prompt += f'[{CliFormatter.GREEN}{option_index}{CliFormatter.END}] {option_text}\n'

    print(solution_prompt)
    return int(input(''))


def exhibit_puzzle_board(puzzle_board):
    for row in puzzle_board:
        row_string = ''
        for item in row:
            value_to_print = f'{CliFormatter.CYAN}{item}' if item else f'{CliFormatter.YELLOW}_'
            row_string += f'{value_to_print}\t'
        row_string += '\n'
        print(row_string, end='')
    print(CliFormatter.END)


def get_user_void_square_choice():
    return input(
        'Em qual quadrado deseja pôr o valor vazio? Obs.: insira o valor numérico,'
        ' e não sua posição na matriz'
    )


def confirm_user_void_square_choice(void_square_value):
    return input(
        f'Deseja mesmo usar a casa cujo valor é'
        f' {CliFormatter.CYAN}{void_square_value}{CliFormatter.END}? (s/n)\n'
    )


def warn_uniform_cost_slowness():
    print(
        '\n'
        f'{CliFormatter.RED}Aviso{CliFormatter.END}: Caso a matriz seja maior que 3x3, '
        f'a solução de busca por Custo Uniforme pode demorar em sua execução.'
        f'\n'
    )


def prompt_for_path_exhibition():
    return input(
        f'{CliFormatter.GREEN}Deseja visualizar o caminho trilhado? (s/n){CliFormatter.END}\n'
    )


def prompt_for_puzzle_board_reuse():
    return input(
        f'{CliFormatter.GREEN}Deseja re-utilizar o tabuleiro para outra busca? (s/n){CliFormatter.END}\n'
    )


def prompt_for_hard_shuffle():
    return input(
        f'Deseja embaralhar no nível {CliFormatter.YELLOW}Fácil{CliFormatter.END} '
        f'ou {CliFormatter.RED}Difícil?{CliFormatter.END} '
        f'({CliFormatter.YELLOW}f{CliFormatter.END}/{CliFormatter.RED}d{CliFormatter.END})\n'
    )


def exhibit_search_info(search_info: SearchInfo, time_taken, solution_type):
    print(f'\n{CliFormatter.CYAN}Solução encontrada em {time_taken} segundos utilizando {solution_type}{CliFormatter.END}')
    print(f'Nodos expandidos: {CliFormatter.YELLOW}{search_info.expanded_nodes}{CliFormatter.END}')
    print(f'Nodos visitados: {CliFormatter.YELLOW}{search_info.visited_nodes}{CliFormatter.END}')
    print(f'Maior tamanho da fronteira: {CliFormatter.YELLOW}{search_info.largest_frontier_size}{CliFormatter.END}')
    print(f'Tamanho do caminho trilhado: {CliFormatter.YELLOW}{len(search_info.path)}{CliFormatter.END}')


def display_program_start():
    print(f'{CliFormatter.GREEN}Busca iniciada!{CliFormatter.END}')


def exhibit_search_path(search_path):
    for node in search_path:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        exhibit_puzzle_board(node.puzzle_board)
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        time.sleep(0.25)


def prompt_user_for_tile_value():
    return int(
        input('Qual o valor da próxima casa do tabuleiro?')
    )


def warn_user_of_repeated_value(value_limit):
    print(f'Você já inseriu este valor! Use outro número não repetido entre 1 e {value_limit}')
