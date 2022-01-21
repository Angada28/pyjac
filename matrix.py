from typing import Union


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
    coefficients: list[list[Union[int, float]]]

    def __init__(self, coefficients: list[list[Union[int, float]]]) -> None:
        """Initialize a new matrix with len(<matrix>) rows and len(<matrix>[0])
        columns
        """
        self.coefficients = coefficients

    def __str__(self) -> str:
        """Prints out a string representation of the matrix
        """
        s = ''
        for i in range(len(self.coefficients)):
            s = s + str(self.coefficients[i]) + '\n'
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


class AugmentedMatrix(CoefficientMatrix):
    """An augmented matrix is a coefficient matrix with an extra column that
    contains the constants of the system of linear equation it represents

    === Attributes ===
    coefficients: the list of lists of coefficients that make up the matrix
    constants: the list of values that contains the constants

    === Representation Invariants ===
    - len(coefficients) == len(constants)
    """
    coefficients: CoefficientMatrix
    constants: list[Union[int, float]]

    def __init__(self, coefficients: CoefficientMatrix,
                 constants: list[Union[int, float]]) -> None:
        CoefficientMatrix.__init__(self, coefficients)
        self.constants = constants

    def __str__(self) -> str:
        s = ''
        for i in range(len(self.constants)):
            s = s + str(self.coefficients.coefficients[i]) + '[' + \
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
