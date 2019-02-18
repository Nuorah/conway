import numpy as np
from matrixtofile import file_to_matrix, matrix_to_file

def sum_around_cell(x, y, matrix):
    return matrix[x - 1, y - 1] + matrix[x - 1, y] + matrix[x - 1, (y + 1) % width] + matrix[x, (y + 1) % width] + matrix[(x + 1) % height, (y + 1) % width] + matrix[(x + 1) % height, y] + matrix[(x + 1) % height, y - 1] + matrix[x, y - 1]

def decide_next_cell(x, y, matrix):
    sum = sum_around_cell(x, y, matrix)
    if matrix[x, y] == 0:
        if sum == 3:
            return 1
        else:
            return 0
    else:
        if sum == 2 or sum == 3:
            return 1
        else:
            return 0

def update_file(filename):
    matrix = file_to_matrix(filename)
    new_matrix = np.zeros(matrix.shape, dtype=int)
    it = np.nditer(matrix, flags=['multi_index'])
    while not it.finished:
        new_matrix[it.multi_index[0], it.multi_index[1]] = decide_next_cell(it.multi_index[0], it.multi_index[1], matrix)
        it.iternext()
    matrix_to_file(new_matrix)

def generate_random_initial_file(height, width):
    matrix = np.random.randint(2, size=(height, width))
    matrix_to_file(matrix)

generate_random_initial_file(20, 20)

