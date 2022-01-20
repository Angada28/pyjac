# pyjac file/functions
from matrix import Matrix


def determinant(m: Matrix):
    """
    computes the determinant of an n x n matrix
    """
    size = len(m.matrix)
    swaps = 0
    for x in m.matrix:
        if len(x) != size:
            return "please input a valid n x n matrix"
    if size == 0:
        return 1
    elif size == 1:
        return m.matrix[0]
    elif size == 2:
        return (m.matrix[0][0] * m.matrix[1][1]) - (
                    m.matrix[0][1] * m.matrix[1][0])
    elif size == 3:
        return m.matrix[0][0] * (
                m.matrix[1][1] * m.matrix[2][2] - m.matrix[1][2] * m.matrix[2][
            1]) - m.matrix[0][1] * (
                           m.matrix[1][0] * m.matrix[2][2] - m.matrix[1][2] *
                           m.matrix[2][0]) + m.matrix[0][2] * (
                           m.matrix[1][0] * m.matrix[2][1] - m.matrix[1][1] *
                           m.matrix[2][0])
    for i in range(size):
        for j in range(i + 1, size):
            if m.matrix[i][i] == 0:
                swaps += swap(m.matrix, i, size)
            if m.matrix[i][i] == 0:
                return 0
            factor = - m.matrix[j][i] / m.matrix[i][i]
            for k in range(i, size):
                m.matrix[j][k] += factor * m.matrix[i][k]
    sum_diagonals = m.matrix[0][0]
    for i in range(size):
        sum_diagonals *= m.matrix[i][i]
    return sum_diagonals * (-1) ** swaps


def swap(new_m: Matrix, col, end_row):
    """
    swaps a row of the matrix and returns either 0 if no swaps occurred or 1 if
    a swap did occur
    """
    for i in range(col, end_row):
        if new_m.matrix[i][col] != 0:
            new_m.matrix[col], new_m.matrix[i] = new_m.matrix[i], new_m.matrix[
                col]
            return 1
    return 0
