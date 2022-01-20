# pyjac file/functions
import copy

from matrix import Matrix
from fractions import *


def determinant(mat: Matrix):
    """
    computes the determinant of an n x n matrix
    """
    # Create a copy of the input
    m = Matrix(copy.deepcopy(mat.matrix))
    size = len(m.matrix)
    swaps = 0
    # Check to see if this is an n x n matrix
    for x in m.matrix:
        if len(x) != size:
            return "please input a valid n x n matrix"
    # When there is an empty matrix return 1
    if size == 0:
        return 1
    # If there is a matrix of size one return the single value
    elif size == 1:
        return m.matrix[0]
    # If the matrix is of size 2 use the formula
    elif size == 2:
        return (m.matrix[0][0] * m.matrix[1][1]) - (
                m.matrix[0][1] * m.matrix[1][0])
    # If the matrix is of size 3 use the formula
    elif size == 3:
        return m.matrix[0][0] * (
                m.matrix[1][1] * m.matrix[2][2] - m.matrix[1][2] * m.matrix[2][
            1]) - m.matrix[0][1] * (
                       m.matrix[1][0] * m.matrix[2][2] - m.matrix[1][2] *
                       m.matrix[2][0]) + m.matrix[0][2] * (
                       m.matrix[1][0] * m.matrix[2][1] - m.matrix[1][1] *
                       m.matrix[2][0])
    # Convert all the entries of the matrix into Fraction() objects
    for i in range(size):
        for j in range(size):
            if type(m.matrix[i][j]) is int:
                m.matrix[i][j] = Fraction(m.matrix[i][j], 1)
            else:
                m.matrix[i][j] = Fraction.from_float(m.matrix[i][j])
    # start converting the matrix into an upper triangle matrix
    for i in range(size):
        for j in range(i + 1, size):
            if m.matrix[i][i] == 0:
                swaps += swap(m, i, size)
            if m.matrix[i][i] == 0:
                return 0
            factor = - m.matrix[j][i] / m.matrix[i][i]
            for k in range(i, size):
                m.matrix[j][k] += factor * m.matrix[i][k]
    # Initialize the product of the diagonal entries and multiply all the
    # entries
    prod_diagonals = m.matrix[0][0]
    for i in range(size):
        prod_diagonals *= m.matrix[i][i]
    prod_diagonals = prod_diagonals * (-1) ** swaps
    if prod_diagonals.denominator == 1:
        return int(prod_diagonals)
    return "determinant is {deter} or about {frac}".format(deter=prod_diagonals,
                                                           frac=float(
                                                               prod_diagonals))


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
