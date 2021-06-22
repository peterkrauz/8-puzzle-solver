from random import shuffle


def solve_puzzle():
    puzzle_input = get_input_matrix()
    puzzle_board = get_puzzle_board(puzzle_input)
    puzzle_board = assign_void_value_to_puzzle_board(puzzle_board)

    print(puzzle_board)


def get_input_matrix():
    input_file = open('input.txt', 'r')
    puzzle_input = input_file.read().split(',')
    input_file.close()
    shuffle(puzzle_input)
    return puzzle_input


def get_puzzle_board(puzzle_input):
    matrix_size = 3
    puzzle_board = [[] for _ in range(int(len(puzzle_input) / matrix_size))]
    for index, item in enumerate(puzzle_input):
        puzzle_board[index % 3].append(item)

    return puzzle_board


def assign_void_value_to_puzzle_board(puzzle_board):
    searching_for_void_square = True
    while searching_for_void_square:

        print(puzzle_board)
        void_square_value = input('Qual quadrado deseja pôr o valor vazio?')
        user_choice = input(f'Deseja mesmo usar o quadrado {void_square_value}? (s/n)')

        if user_choice == 's':
            row, column = find_index_for_value(puzzle_board, void_square_value)
            puzzle_board[row][column] = None
            return puzzle_board


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
