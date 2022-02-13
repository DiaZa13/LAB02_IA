from sudoku import solve

Node = int
Weight = int
Vertices = list[list[[Node, Weight]]]

def readGraph(file):
    with open(file, 'r') as graph:
        node_count = int(graph.readline())
        edges_count = int(graph.readline())
        edges: Vertices = [[] for _ in range(node_count)]
        for edge in graph:
            if edge != '\n':
                x = edge.split()
                edges[int(x[0]) - 1].append((int(x[1]) - 1, int(x[2])))
    return node_count, edges_count, edges


def readSudoku(file):
    with open(file, 'r') as sudoku:
        size = int(sudoku.readline())
        restrictions_count = int(sudoku.readline())
        board = [[0 for _ in range(size)] for _ in range(size)]
        for restriction in sudoku:
            if restriction != '\n':
                x = restriction.split()
                board[int(x[0]) - 1][int(x[1]) - 1] = int(x[2])
    return size, restrictions_count, board


def print_sudoku(sudoku, size, writer):
    if size == 6:
        square_height = 2
        square_length = 3
    elif size == 9:
        square_height = 3
        square_length = 3
    else:
        square_height = 2
        square_length = 2

    line_format = ' |'.join([' {}' * square_length for _ in range(square_height)]) + '\n'
    separator = '-' * (2 * (size + square_length - 1) + 1) + '\n'
    result = []

    for i in range(square_length):
        line = ''
        for j in range(square_height):
            line += line_format.format(*sudoku[i * square_height + j])
        result.append(line)
    writer.write(separator.join(result))


def writeSudoku(file, board, size: int):
    with open(file, 'w') as sudoku:
        count = 1
        for solution in solve(board, size):
            sudoku.write(f'Solution #{count}\n')
            print_sudoku(solution, size, sudoku)
            sudoku.write('\n')
            count += 1
