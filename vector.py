from typing import Union


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
    vector: list[Union[int, float]]

    def __init__(self, vector: list[Union[int, float]]) -> None:
        """Initialize a new vector with len(<vector>) rows and 1 column

        >>> V = Vector([5, 2, 3])
        >>> V.vector
        [5, 2, 3]
        """
        # TODO: Write implementation
        pass

    def __str__(self) -> str:
        """Prints out a string representation of the vector

        >>> V = Vector(0, -1, 1)
        >>> V
        '[0]
         [-1]
         [1]'
        """
        # TODO: Write implementation
        pass

    def __eq__(self, other) -> bool:
        """Returns if the vector <self> is equal in value to the vector <other>

        >>> A = Vector([1, 1])
        >>> B = Vector([1, 1])
        >>> A == B
        True
        """
        # TODO: Write implementation
        pass
