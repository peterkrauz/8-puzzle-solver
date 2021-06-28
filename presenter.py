from solution_type import SolutionType


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
    matrix_size = int(input('Qual o tamanho do lado da matriz desejada?'))
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
        for item in row:
            value_to_print = f'{CliFormatter.CYAN}{item}' if item else f'{CliFormatter.YELLOW}_'
            print(f'{value_to_print}\t', end='')
        print()
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
