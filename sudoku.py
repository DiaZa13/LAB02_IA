from copy import deepcopy

# Para no tener que escribirlo varias veces y que mi linter me siga ayudando
Sudoku = list[list[int]]

SQUARE_HEIGHT = 3
SQUARE_LENGTH = 3
SIZE = SQUARE_LENGTH * SQUARE_HEIGHT

test = [
    [9, 2, 6, 5, 7, 1, 4, 8, 3],
    [3, 5, 1, 4, 8, 6, 2, 7, 9],
    [8, 7, 4, 9, 2, 3, 5, 1, 6],
    [5, 8, 2, 3, 6, 7, 1, 9, 4],
    [1, 4, 9, 2, 5, 8, 3, 6, 7],
    [7, 6, 3, 1, 0, 0, 8, 2, 5],
    [2, 3, 8, 7, 0, 0, 6, 5, 1],
    [6, 1, 7, 8, 3, 5, 9, 4, 2],
    [4, 9, 5, 6, 1, 2, 7, 3, 8],
]
'''
test = [
    [2, 1, 3, 0, 0, 0],
    [4, 5, 6, 0, 2, 0],
    [0, 0, 0, 6, 1, 4],
    [0, 0, 0, 3, 5, 2],
    [6, 4, 5, 0, 0, 0],
    [3, 2, 1, 0, 4, 0]
]
'''


def find_empty(sudoku: Sudoku) -> [int, int]:
    for y in range(SIZE):
        for x in range(SIZE):
            if sudoku[y][x] == 0:
                return x, y

    return None


def find_options(x: int, y: int, sudoku: Sudoku) -> list[int]:
    return [i for i in range(1, SIZE + 1) if is_valid(sudoku, x, y, i)]


def column(sudoku: Sudoku, n: int) -> list[int]:
    return [i[n] for i in sudoku]


def row(sudoku: Sudoku, n: int) -> list[int]:
    return sudoku[n]


def square(sudoku: Sudoku, x: int, y: int) -> list[int]:
    top = y // SQUARE_HEIGHT * SQUARE_HEIGHT
    start = x // SQUARE_LENGTH * SQUARE_LENGTH
    box = []

    for i in range(SQUARE_HEIGHT):
        box.extend(sudoku[top + i][start:start + SQUARE_LENGTH])

    return box


def is_valid(sudoku: Sudoku, x: int, y: int, n: int) -> bool:
    return not (
            n in row(sudoku, y) or
            n in column(sudoku, x) or
            n in square(sudoku, x, y)
    )


# Creo que esto me tardó más tiempo que hacer el resto del programa xd
def print_sudoku(sudoku: Sudoku):
    line_format = ' |'.join([' {}' * SQUARE_LENGTH for _ in range(SQUARE_HEIGHT)]) + '\n'
    separator = '-' * (2 * (SIZE + SQUARE_LENGTH - 1) + 1) + '\n'
    result = []

    for i in range(SQUARE_LENGTH):
        line = ''
        for j in range(SQUARE_HEIGHT):
            line += line_format.format(*sudoku[i * SQUARE_HEIGHT + j])
        result.append(line)
    print(separator.join(result))


def solve(sudoku: Sudoku) -> list[Sudoku]:
    empty_spot = find_empty(sudoku)

    if empty_spot is None:
        return [sudoku]
    else:
        x, y = empty_spot
        solutions: list[Sudoku] = []

        for option in find_options(x, y, sudoku):
            copy = deepcopy(sudoku)
            copy[y][x] = option
            solutions.extend(solve(copy))
        return solutions


for solution in solve(test):
    print_sudoku(solution)
    print()
