from random import shuffle


def solve_puzzle():
    puzzle_input = get_input_matrix()
    puzzle_board = get_puzzle_board(puzzle_input)
    puzzle_board = assign_void_value_to_puzzle_board(puzzle_board)

    solution_type = get_solution_type()

    exhibit_puzzle_board(puzzle_board)


def get_solution_type():
    print('Deseja rodar o programa em qual dos seguintes modos?')
    print('[1] Custo Uniforme')
    print('[2] A* com heurística simples')
    print('[3] A* com heurística precisa')
    return int(input(''))


def get_input_matrix():
    input_file = open('initial_board.txt', 'r')
    puzzle_input = input_file.read().split(',')
    input_file.close()
    shuffle(puzzle_input)
    return puzzle_input


def get_puzzle_board(puzzle_input):
    matrix_size = 3
    puzzle_board = [[] for _ in range(int(len(puzzle_input) / matrix_size))]
    for index, item in enumerate(puzzle_input):
        puzzle_board[index % 3].append(int(item.strip()))

    return puzzle_board


def assign_void_value_to_puzzle_board(puzzle_board):
    searching_for_void_square = True
    while searching_for_void_square:

        exhibit_puzzle_board(puzzle_board)
        void_square_value = int(
            input(
                'Em qual quadrado deseja pôr o valor vazio? Obs.: insira o valor numérico,'
                ' e não sua posição na matriz'
            )
        )
        user_choice = input(f'Deseja mesmo usar o quadrado \033[94m{void_square_value}\033[0m? (s/n)\n')

        if user_choice == 's':
            row, column = find_index_for_value(puzzle_board, void_square_value)
            puzzle_board[row][column] = None
            return puzzle_board


def exhibit_puzzle_board(puzzle_board):
    for row in puzzle_board:
        for item in row:
            value_to_print = f'\033[94m{item}' if item else '\033[93m_'
            print(f'{value_to_print} ', end='')
        print()
    print('\033[0m')


def find_index_for_value(puzzle_board, value):
    row_index = 0
    for row in puzzle_board:
        column_index = 0
        for column in row:
            if column == value:
                return row_index, column_index
            column_index += 1
        row_index += 1


if __name__ == '__main__':
    solve_puzzle()
