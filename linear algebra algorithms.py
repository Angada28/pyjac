# pyjac file/functions
import copy

from matrix import *
from fractions import *
from vector import Vector
from typing import List, Union


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


def cross_product(first: Vector, second: Vector) -> Vector:
    """
    pre: first and second are valid vectors in r3 with real components
    post: returns a new vector that is perpendicular to both first and second
    """
    new_vector = [
        first.vector[1] * second.vector[2] - first.vector[2] * second.vector[1],
        first.vector[2] * second.vector[0] - first.vector[0] * second.vector[2],
        first.vector[0] * second[1] - first.vector[1] * second.vector[0]]
    v = Vector(new_vector)
    return v


def dot_product(first: Vector, second: Vector):
    """
    pre: first and second are valid vectors of the same size
    post: returns the dot product of first and second
    """
    total = 0
    for i in range(len(first.vector)):
        total += first.vector[i] * second.vector[i]
    return total


def get_inverse(mat: CoefficientMatrix) -> Union[None, CoefficientMatrix]:
    """
    Returns the inverse of the matrix if it is invertible.
    """
    mat_a = CoefficientMatrix(copy.deepcopy(mat.coefficients))

    # Initializing indices. j is the column that holds a leading one
    i = 0
    j = 0
    # Assigning number of rows and columns to m an n respectively
    m = len(mat_a.coefficients)
    n = len(mat_a.coefficients[0])
    # Check if there are the same number of rows and columns
    if m != n:
        print("Matrix is not invertible. It needs to be an NxN matrix.")
        return None
    # Make an identity matrix of NxN and a Matrix that will be the inverse
    identity_mat = CoefficientMatrix([])
    mat_b = CoefficientMatrix([])

    for row in range(n):
        identity_mat.coefficients.append([])
        mat_b.coefficients.append([])
        for col in range(n):
            if row == col:
                identity_mat.coefficients[row].append(1)
                mat_b.coefficients[row].append(1)
            else:
                identity_mat.coefficients[row].append(0)
                mat_b.coefficients[row].append(0)

    # Row reduction algorithm for getting matrix A into RREF while giving
    # matrix B the same operations
    while i < m and j < n:
        # check if the following rows after the current row have a non-zero
        # coefficient in the current column and swap if one is found,
        # otherwise check in the next column
        _swap = False
        new_row = None
        if mat_a.coefficients[i][j] == 0:
            while j < n and not _swap:
                row = i
                while row < m and not _swap:
                    if mat_a.coefficients[row][j] != 0:
                        _swap = True
                        new_row = row
                    row += 1
                if not _swap:
                    j += 1
            if _swap:
                mat_a.swap_rows(i + 1, new_row + 1)
                mat_b.swap_rows(i + 1, new_row + 1)
            else:
                break

        # Dividing row by leading number to get a leading one
        col = 0
        d = Fraction(str(mat_a.coefficients[i][j]))
        while col < n:
            mat_a.coefficients[i][col] =\
                Fraction(str(mat_a.coefficients[i][col])) / d
            mat_b.coefficients[i][col] =\
                Fraction(str(mat_b.coefficients[i][col])) / d
            col += 1

        # Row reducing so all numbers in the column of this row's leading one
        # will be 0
        row = 0
        while row < m:
            if row != i:
                c = Fraction(str(mat_a.coefficients[row][j]
                                 / mat_a.coefficients[i][j]))
                col = 0
                while col < n:
                    mat_a.coefficients[row][col] =\
                        Fraction(str(mat_a.coefficients[row][col])) - \
                        c * Fraction(str(mat_a.coefficients[i][col]))
                    mat_b.coefficients[row][col] =\
                        Fraction(str(mat_b.coefficients[row][col])) - \
                        c * Fraction(str(mat_b.coefficients[i][col]))
                    col += 1
            row += 1

        i += 1
        j += 1

    if identity_mat == mat_a:
        return mat_b
    print("Matrix is not invertible.")
    return None


def get_rref(mat: AugmentedMatrix) -> AugmentedMatrix:
    """
    Returns a row reduced echelon form of the Matrix.
    """
    mat_a = AugmentedMatrix(copy.deepcopy(mat.coefficients),
                            copy.deepcopy(mat.constants))

    # Initializing indices. j is the column that holds a leading one
    i = 0
    j = 0
    m = len(mat_a.constants)

    # Assigning number of rows and columns to m an n respectively
    if m > 0:
        n = len(mat_a.coefficients.coefficients[0])
    else:
        n = 0

    coefficient_mat = mat_a.coefficients.coefficients

    # Row reduction algorithm for getting matrix into RREF
    while i < m and j < n:
        # check if the following rows after the current row have a non-zero
        # coefficient in the current column and swap if one is found,
        # otherwise check in the next column
        _swap = False
        new_row = None
        if coefficient_mat[i][j] == 0:
            while j < n and not _swap:
                row = i
                while row < m and not _swap:
                    if coefficient_mat[row][j] != 0:
                        _swap = True
                        new_row = row
                    row += 1
                if not _swap:
                    j += 1

            if _swap:
                mat_a.swap_rows(i + 1, new_row + 1)
                # Printing the previous row reduction step
                print("==> R_"+str(i) + " <-> " + "R_"+str(new_row))
                print(mat_a)
            else:
                return mat_a
        # Dividing row by leading number to get a leading one
        col = 0
        d = Fraction(str(coefficient_mat[i][j]))
        while col < n:
            coefficient_mat[i][col] =\
                Fraction(str(coefficient_mat[i][col])) / d
            col += 1
        mat_a.constants[i] = Fraction(str(mat_a.constants[i])) / d
        # Printing the previous row reduction step
        if d != 1:
            print("==> (" + str(Fraction(str(1/d))) + ')R_' + str(i))
            print(str(mat_a) + '\n')

        # Row reducing so all numbers in the column of this row's leading one
        # will be 0
        row = 0
        while row < m:
            if row != i:
                c = Fraction(str(coefficient_mat[row][j] /
                                 coefficient_mat[i][j]))
                col = 0
                while col < n:
                    coefficient_mat[row][col] =\
                        Fraction(str(coefficient_mat[row][col])) - \
                        c * Fraction(str(coefficient_mat[i][col]))
                    col += 1
                mat_a.constants[row] =\
                    Fraction(str(mat_a.constants[row])) - \
                    c * Fraction(str(mat_a.constants[i]))

                # Printing the previous row reduction step
                if c != 0:
                    print("==> R_" + str(row) + " - " +
                          "(" + str(Fraction(str(1/d))) + ')R_' + str(i))
                    print(str(mat_a) + '\n')
            row += 1
        i += 1
        j += 1

    return mat_a


def is_consistent(mat: AugmentedMatrix) -> bool:
    """
    Checks if the Augmented Matrix is Consistent.
    """

    for i in range(len(mat.coefficients.coefficients) - 1, -1, -1):
        j = 0

        all_zero = True
        curr_row = mat.coefficients.coefficients[i]
        while j < len(curr_row):
            if curr_row[j] != 0:
                all_zero = False
                j = len(curr_row)
            j += 1

        if all_zero:
            if mat.constants[i] != 0:
                return False
    return True


def gaussian(mat: AugmentedMatrix) -> str:
    """
    Uses Gaussian Elimination to solve the given system of equations.
    """
    mat_a = get_rref(mat)

    if not is_consistent(mat_a):
        return "No solutions. Linear system is inconsistent."

    # Separate the coefficients and the constants in two different lists
    _coefficients = mat_a.coefficients.coefficients
    _constants = mat_a.constants

    # Get the number of rows and columns of the coefficient Matrix
    m = len(_coefficients)
    n = 0
    if m > 0:
        n = len(_coefficients[0])

    # collect all the leading variables
    leading = []
    leading_cols = []
    row = 0
    while row < m:
        col = 0
        while col < n:
            if _coefficients[row][col] != 0:
                leading.append((col, []))
                leading_cols.append(col)
                col = n
            col += 1
        row += 1

    # basic solutions
    basic_sols = [[]]

    # free variables
    free_vars = []

    # Collect the free variables
    for i in range(n):
        if i not in leading_cols:
            free_vars.append(i)

    # Add a list in the basic solutions for every free variable
    for i in range(len(free_vars)):
        basic_sols.append([])

    # collect all the free variable's coefficients and all the constants
    # corresponding to the leading variables
    for i in range(len(leading)):
        for j in free_vars:
            leading[i][1].append(-_coefficients[i][j])
        leading[i][1].append(_constants[i])

    for i in range(len(basic_sols)):
        c = 0
        for j in range(n - 1):
            d = 0
            if j in free_vars:
                if d != i or i == len(basic_sols) - 1:
                    basic_sols[i].append(0)
                else:
                    basic_sols[i].append(1)
                d += 1
            else:
                basic_sols[i].append(leading[c][1][i])
                c += 1

    leading_str = ""
    free_str = ""
    for i in leading:

        curr = "X_" + str(i[0] + 1) + " ="
        free_str = ""
        for j in range(len(free_vars)):
            if i[1][j] != 0:
                curr += " (" + str(i[1][j]) + ") S_" + str(j + 1) + " +"
            free_str += "X_" + str(free_vars[j] + 1) + " = S_" + str(j + 1) +\
                        "\n"

        if i[1][-1] != 0:
            curr += " " + str(i[1][-1])
        else:
            curr = curr[0: -2]

        if '=' not in curr:
            curr += " = 0"

        curr += "\n"
        leading_str += curr

    if leading_str + free_str == "":
        return "No solutions."
    return leading_str + free_str
