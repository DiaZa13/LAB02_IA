from copy import deepcopy

Sudoku = list[list[int]]

def find_empty(sudoku: Sudoku, size) -> [int, int]:
    for y in range(size):
        for x in range(size):
            if sudoku[y][x] == 0:
                return x, y

    return None


def find_options(x: int, y: int, sudoku: Sudoku, size) -> list[int]:
    if size == 6:
        square_height = 2
        square_length = 3
    elif size == 9:
        square_height = 3
        square_length = 3
    else:
        square_height = 2
        square_length = 2
    return [i for i in range(1, size + 1) if is_valid(sudoku, x, y, i, square_height, square_length)]


def column(sudoku: Sudoku, n: int) -> list[int]:
    return [i[n] for i in sudoku]


def row(sudoku: Sudoku, n: int) -> list[int]:
    return sudoku[n]


def square(sudoku: Sudoku, x: int, y: int, square_height: int, square_length: int) -> list[int]:
    top = y // square_height * square_height
    start = x // square_length * square_length
    box = []

    for i in range(square_height):
        box.extend(sudoku[top + i][start:start + square_length])

    return box


def is_valid(sudoku: Sudoku, x: int, y: int, n: int, square_height: int, square_length: int) -> bool:
    return not (
            n in row(sudoku, y) or
            n in column(sudoku, x) or
            n in square(sudoku, x, y, square_height, square_length)
    )

def solve(sudoku: Sudoku, size: int) -> list[Sudoku]:
    empty_spot = find_empty(sudoku, size)
    if empty_spot is None:
        return [sudoku]
    else:
        x, y = empty_spot
        solutions: list[Sudoku] = []

        for option in find_options(x, y, sudoku, size):
            copy = deepcopy(sudoku)
            copy[y][x] = option
            solutions.extend(solve(copy, size))
        return solutions

