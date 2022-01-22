from typing import Union, List


class Vector:
    """A vector that contains m numbers and 1 column

    === Attributes ===
    vector: the list of values that make up the vector

    === Sample Usage ===
    Creating a vector:
    >>> V = Vector([0, 1, 2])
    >>> V
    '[0]
     [1]
     [2]'
    """
    vector: List[Union[int, float]]

    def __init__(self, vector: List[Union[int, float]]) -> None:
        """Initialize a new vector with len(<vector>) rows and 1 column

        >>> V = Vector([5, 2, 3])
        >>> V.vector
        [5, 2, 3]
        """
        self.vector = vector

    def __str__(self) -> str:
        """Prints out a string representation of the vector

        >>> V = Vector(0, -1, 1)
        >>> V
        '[0]
         [-1]
         [1]'
        """
        s = ''
        for num in self.vector:
            s = s + '[' + str(num) + ']\n'
        return s.strip()

    def __eq__(self, other) -> bool:
        """Returns True if the vector <self> is equal in value to the vector
        <other>

        >>> A = Vector([1, 1])
        >>> B = Vector([1, 1])
        >>> A == B
        True
        """
        return self.vector == other.vector

    def __ne__(self, other) -> bool:
        """Returns True if the vector <self> is not equal in value to the vector
        <other>

        >>> A = Vector([1, 1])
        >>> B = Vector([1, 1])
        >>> A != B
        False
        """
        return self.vector != other.vector
