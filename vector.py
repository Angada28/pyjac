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

    def cross_product(self, other: 'Vector') -> 'Vector':
        """
        pre: first and second are valid vectors in r3 with real components
        post: returns a new vector that is perpendicular to both first and second
        """
        new_vector = [
            self.vector[1] * other.vector[2] - self.vector[2] * other.vector[1],
            self.vector[2] * other.vector[0] - self.vector[0] * other.vector[2],
            self.vector[0] * other.vector[1] - self.vector[1] * other.vector[0]]
        v = Vector(new_vector)
        return v

    def dot_product(self, other: 'Vector'):
        """
        pre: first and second are valid vectors of the same size
        post: returns the dot product of first and second
        """
        total = 0
        for i in range(len(self.vector)):
            total += self.vector[i] * other.vector[i]
        return total
