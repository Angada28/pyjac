from typing import Union


class ComplexNumber:
    """A complex number with a real component and an imaginary component

    === Attributes ===
    real: the real component of the complex number
    imaginary: the imaginary component of the complex number

    === Sample Usage ===
    Creating a complex number:
    >>> c = ComplexNumber(5, 3)
    >>> str(c)
    '5i+3'
    >>> c0 = ComplexNumber(-4, -2)
    >>> str(c0)
   '-4i-2'
    """
    real: Union[int, float]
    imaginary: Union[int, float]

    def __init__(self, imaginary: Union[int, float], real: Union[int, float]) \
            -> None:
        """Initialize a new complex number with a real component with value
        <real> and an imaginary component with value <imaginary>

        >>> c = ComplexNumber(5, 7)
        >>> c.real
        5
        >>> c.imaginary
        7
        """
        self.real = real
        self.imaginary = imaginary

    def __str__(self) -> str:
        """Prints out a string representation of the complex number

        >>> c = ComplexNumber(4, -9)
        >>> c
        '4i-9'
        """
        if self.imaginary == -1:
            return '-i' + self._string_helper()
        return (str(self.imaginary) + 'i' + self._string_helper()).lstrip('1')

    def __eq__(self, other) -> bool:
        """Returns if the complex number <self> is equal in value to the complex
        number <other>

        >>> c1 = ComplexNumber(5, 6)
        >>> c2 = ComplexNumber(5, 6)
        >>> c1 == c2
        True
        """
        return (self.real == other.real) and (self.imaginary == other.imaginary)

    def __ne__(self, other) -> bool:
        """Returns if the complex number <self> is not equal in value to the
        complex number <other>

        >>> c1 = ComplexNumber(5, -6)
        >>> c2 = ComplexNumber(-5, 6)
        >>> c1 != c2
        True
        """
        return (self.real != other.real) or (self.imaginary != other.imaginary)

    def _string_helper(self) -> str:
        """Private helper function for the __str__ magic method

        Helps add a plus sign, minus sign, or no number in the string
        """
        if self.real > 0:
            return '+' + str(self.real)
        elif self.real < 0:
            return str(self.real)
        return ''
