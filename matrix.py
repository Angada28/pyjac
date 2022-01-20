from typing import Union
from typing import List


class Matrix:
    """A matrix with m rows and n columns

    === Attributes ===
    matrix: the list of lists of values that make up the matrix

    === Sample Usage ===
    Creating a matrix:
    >>> A = Matrix([[1, 3, 0], [0, 2, 5], [4, 2, 0]])
    >>> A
    '[1  3  0]
     [0  2  5]
     [4  2  0]'
    """
    matrix: List[List[Union[int, float]]]

    def __init__(self, matrix: List[List[Union[int, float]]]) -> None:
        """Initialize a new matrix with len(<matrix>) rows and len(<matrix>[0])
        columns

        >>> M = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        >>> M.matrix
        [[1  2  3], [4  5  6], [7  8  9]]
        """
        self.matrix = matrix

    def __str__(self) -> str:
        """Prints out a string representation of the matrix

        >>> M = Matrix([[1, 2, 3], [4, 5, 6]])
        >>> M
        '[1  2  3]
         [4  5  6]'
        """
        return str(self.matrix)

    def __eq__(self, other) -> bool:
        """Returns if the matrix <self> is equal in value to the matrix <other>

        >>> A = Matrix([1, 2], [3, 4])
        >>> B = Matrix([1, 2], [3, 4])
        >>> A == B
        True
        """
        return self.matrix == other.matrix

