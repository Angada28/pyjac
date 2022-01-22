from typing import Union, List
from fractions import Fraction
import copy


class Matrix:
    """A matrix can either be an mxn coefficient matrix or an mx(n+1) augmented
    matrix

    This is an abstract class and shouldn't be instantiated

    """

    def __init__(self) -> None:
        """Initialize a new matrix with len(<matrix>) rows and len(<matrix>[0])
        columns
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """Prints out a string representation of the matrix
        """
        raise NotImplementedError

    def __eq__(self, other) -> bool:
        """Returns if the matrix <self> is equal in value to the matrix <other>
        """
        raise NotImplementedError

    def __ne__(self, other) -> bool:
        """Returns if the matrix <self> is not equal in value to the matrix
        <other>
        """
        raise NotImplementedError

    def swap_rows(self, row1: int, row2: int) -> None:
        """Swaps rows <row1> and <row2>
        """
        raise NotImplementedError


class CoefficientMatrix(Matrix):
    """A coefficient matrix is a matrix that contains the coefficients of a
    system of linear equations

    === Attributes ===
    coefficients: the list of lists of coefficients that make up the matrix
    """
    coefficients: List[List[Union[int, Union[Fraction, float]]]]

    def __init__(self,
                 coefficients:
                 List[List[Union[int, Union[Fraction, float]]]]) -> None:
        """Initialize a new matrix with len(<matrix>) rows and len(<matrix>[0])
        columns
        """
        self.coefficients = coefficients

    def __str__(self) -> str:
        """Prints out a string representation of the matrix
        """
        s = ''
        for i in range(len(self.coefficients)):
            _print = ''
            for j in range(len(self.coefficients[i])):
                _print += str(self.coefficients[i][j]) + ', '
            s = s + '[' + str(_print[:-2]) + ']' + '\n'
        return s.rstrip()

    def __eq__(self, other) -> bool:
        """Returns if the matrix <self> is equal in value to the matrix <other>
        """
        return self.coefficients == other.coefficients

    def __ne__(self, other) -> bool:
        """Returns if the matrix <self> is not equal in value to the matrix
        <other>
        """
        return self.coefficients != other.coefficients

    def swap_rows(self, row1: int, row2: int) -> None:
        """Swaps rows <row1> and <row2>

        === Precondition ===
        - 1 <= <row1> and <row2> <= (len(self.coefficients) - 1)
        """
        row_one = self.coefficients[row1 - 1]
        row_two = self.coefficients[row2 - 1]

        self.coefficients[row1 - 1] = row_two
        self.coefficients[row2 - 1] = row_one

    def determinant(self):
        """
        computes the determinant of an n x n matrix
        """
        # Create a copy of the input
        m = CoefficientMatrix(copy.deepcopy(self.coefficients))
        size = len(m.coefficients)
        swaps = 0
        # Check to see if this is an n x n matrix
        for x in m.coefficients:
            if len(x) != size:
                return "please input a valid n x n matrix"
        # When there is an empty matrix return 1
        if size == 0:
            return 1
        # If there is a matrix of size one return the single value
        elif size == 1:
            return m.coefficients[0]
        # If the matrix is of size 2 use the formula
        elif size == 2:
            return (m.coefficients[0][0] * m.coefficients[1][1]) - (
                    m.coefficients[0][1] * m.coefficients[1][0])
        # If the matrix is of size 3 use the formula
        elif size == 3:
            return m.coefficients[0][0] * (
                    m.coefficients[1][1] * m.coefficients[2][2] -
                    m.coefficients[1][2] * m.coefficients[2][1]) -\
                   m.coefficients[0][1] * (
                           m.coefficients[1][0] * m.coefficients[2][2] -
                           m.coefficients[1][2] * m.coefficients[2][0]) +\
                   m.coefficients[0][2] * (m.coefficients[1][0] *
                                           m.coefficients[2][1] -
                                           m.coefficients[1][1] *
                                           m.coefficients[2][0])
        # Convert all the entries of the matrix into Fraction() objects
        for i in range(size):
            for j in range(size):
                if type(m.coefficients[i][j]) is int:
                    m.coefficients[i][j] = Fraction(m.coefficients[i][j], 1)
                else:
                    m.coefficients[i][j] =\
                        Fraction.from_float(m.coefficients[i][j])
        # start converting the matrix into an upper triangle matrix
        for i in range(size):
            for j in range(i + 1, size):
                if m.coefficients[i][i] == 0:
                    swaps += m._swap(i, size)
                if m.coefficients[i][i] == 0:
                    return 0
                factor = - m.coefficients[j][i] / m.coefficients[i][i]
                for k in range(i, size):
                    m.coefficients[j][k] += factor * m.coefficients[i][k]
        # Initialize the product of the diagonal entries and multiply all the
        # entries
        prod_diagonals = m.coefficients[0][0]
        for i in range(size):
            prod_diagonals *= m.coefficients[i][i]
        prod_diagonals = prod_diagonals * (-1) ** swaps
        if prod_diagonals.denominator == 1:
            return int(prod_diagonals)
        return "determinant is {deter} or about {frac}".format(
            deter=prod_diagonals, frac=float(prod_diagonals))

    def _swap(self, col, end_row):
        """
        swaps a row of the matrix and returns either 0 if no swaps occurred or 1
        if a swap did occur
        """
        for i in range(col, end_row):
            if self.coefficients[i][col] != 0:
                self.coefficients[col], self.coefficients[i] =\
                    self.coefficients[i], self.coefficients[
                    col]
                return 1
        return 0

    def get_inverse(self) -> Union[None, 'CoefficientMatrix']:
        """
        Returns the inverse of the matrix if it is invertible.
        """
        mat_a = CoefficientMatrix(copy.deepcopy(self.coefficients))

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
                mat_a.coefficients[i][col] = \
                    Fraction(str(mat_a.coefficients[i][col])) / d
                mat_b.coefficients[i][col] = \
                    Fraction(str(mat_b.coefficients[i][col])) / d
                col += 1

            # Row reducing so all numbers in the column of this row's
            # leading one will be 0
            row = 0
            while row < m:
                if row != i:
                    c = Fraction(str(mat_a.coefficients[row][j]
                                     / mat_a.coefficients[i][j]))
                    col = 0
                    while col < n:
                        mat_a.coefficients[row][col] = \
                            Fraction(str(mat_a.coefficients[row][col])) - \
                            c * Fraction(str(mat_a.coefficients[i][col]))
                        mat_b.coefficients[row][col] = \
                            Fraction(str(mat_b.coefficients[row][col])) - \
                            c * Fraction(str(mat_b.coefficients[i][col]))
                        col += 1
                row += 1
            i += 1
            j += 1

        if identity_mat == mat_a:
            print("The RREF of the matrix is:")
            return mat_b
        print("Matrix is not invertible.")
        return None


class AugmentedMatrix(Matrix):
    """An augmented matrix is a coefficient matrix with an extra column that
    contains the constants of the system of linear equation it represents

    === Attributes ===
    coefficients: the list of lists of coefficients that make up the matrix
    constants: the list of values that contains the constants

    === Representation Invariants ===
    - len(coefficients) == len(constants)
    """
    coefficients: CoefficientMatrix
    constants: List[Union[int, Union[Fraction, float]]]

    def __init__(self, coefficients: CoefficientMatrix,
                 constants: List[Union[int, Union[Fraction, float]]]) -> None:
        CoefficientMatrix.__init__(self, coefficients)
        self.constants = constants

    def __str__(self) -> str:
        s = ''
        for i in range(len(self.constants)):
            _print = ''
            for j in range(len(self.coefficients.coefficients[i])):
                _print += str(self.coefficients.coefficients[i][j]) + ', '
            s = s + '[' + str(_print[:-2]) + ']' + '[' + \
                str(self.constants[i]) + ']\n'
        return s.rstrip()

    def __eq__(self, other) -> bool:
        return (self.coefficients == other.coefficients) and \
               (self.constants == other.constants)

    def __ne__(self, other) -> bool:
        return (self.coefficients != other.coefficients) or \
               (self.constants != other.constants)

    def swap_rows(self, row1: int, row2: int) -> None:
        """Swaps rows <row1> and <row2>

        === Precondition ===
        - 1 <= <row1> and <row2> <= (len(self.coefficients) - 1)
        """
        self.coefficients.swap_rows(row1, row2)

        row_one = self.constants[row1 - 1]
        row_two = self.constants[row2 - 1]

        self.constants[row1 - 1] = row_two
        self.constants[row2 - 1] = row_one

    def get_rref(self) -> 'AugmentedMatrix':
        """
        Returns a row reduced echelon form of the Matrix.
        """
        mat_a = AugmentedMatrix(copy.deepcopy(self.coefficients),
                                copy.deepcopy(self.constants))

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
                coefficient_mat[i][col] = \
                    Fraction(str(coefficient_mat[i][col])) / d
                col += 1
            mat_a.constants[i] = Fraction(str(mat_a.constants[i])) / d
            # Printing the previous row reduction step
            if d != 1:
                print("==> (" + str(Fraction(str(1/d))) + ')R_' + str(i))
                print(str(mat_a) + '\n')

            # Row reducing so all numbers in the column of this row's leading
            # one will be 0
            row = 0
            while row < m:
                if row != i:
                    c = Fraction(str(coefficient_mat[row][j] /
                                     coefficient_mat[i][j]))
                    col = 0
                    while col < n:
                        coefficient_mat[row][col] = \
                            Fraction(str(coefficient_mat[row][col])) - \
                            c * Fraction(str(coefficient_mat[i][col]))
                        col += 1
                    mat_a.constants[row] = \
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

        print("The RREF of the matrix is:")
        return mat_a

    def is_consistent(self) -> bool:
        """
        Checks if the Augmented Matrix is Consistent.
        """

        for i in range(len(self.coefficients.coefficients) - 1, -1, -1):
            j = 0

            all_zero = True
            curr_row = self.coefficients.coefficients[i]
            while j < len(curr_row):
                if curr_row[j] != 0:
                    all_zero = False
                    j = len(curr_row)
                j += 1

            if all_zero:
                if self.constants[i] != 0:
                    return False
        return True

    def gaussian(self) -> str:
        """
        Uses Gaussian Elimination to solve the given system of equations.
        """
        mat_a = self.get_rref()

        if not mat_a.is_consistent():
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

        # free variables
        free_vars = []

        # Collect the free variables
        for i in range(n):
            if i not in leading_cols:
                free_vars.append(i)

        # collect all the free variable's coefficients and all the constants
        # corresponding to the leading variables
        for i in range(len(leading)):
            for j in free_vars:
                leading[i][1].append(-_coefficients[i][j])
            leading[i][1].append(_constants[i])

        leading_str = ""
        free_str = ""
        for i in leading:

            curr = "X_" + str(i[0] + 1) + " ="
            free_str = ""
            for j in range(len(free_vars)):
                if i[1][j] != 0:
                    curr += " (" + str(i[1][j]) + ") S_" + str(j + 1) + " +"
                free_str += "X_" + str(free_vars[j] + 1) + " = S_" + str(j + 1) + \
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
        return "Solutions:\n" + leading_str + free_str
