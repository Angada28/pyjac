from typing import Union


class ComplexNumber:
    """A complex number with a real component and an imaginary component

    === Attributes ===
    real: the real component of the complex number
    imaginary: the imaginary component of the complex number

    === Sample Usage ===
    Creating a complex number:
    >>> C = ComplexNumber(5, 3)
    >>> C
    '5i + 3'
    >>> C0 = ComplexNumber(-4, -2)
    >>> C0
   '-4i - 2'
    """
    real: Union[int, float]
    imaginary: Union[int, float]

    def __init__(self, real: Union[int, float], imaginary: Union[int, float]) \
            -> None:
        """Initialize a new complex number with a real component with value
        <real> and an imaginary component with value <imaginary>

        >>> C = ComplexNumber(5, 7)
        >>> C.real
        5
        >>> C.imaginary
        7
        """
        # TODO: Write implementation
        pass

    def __str__(self) -> str:
        """Prints out a string representation of the complex number

        >>> C = ComplexNumber(4, -9)
        >>> C
        '4i - 9'
        """
        # TODO: Write implementation
        pass

    def __eq__(self, other) -> bool:
        """Returns if the complex number <self> is equal in value to the complex
        number <other>

        >>> C1 = ComplexNumber(-5, 6)
        >>> C2 = ComplexNumber(5, 6)
        >>> C1 == C2
        False
        """
        # TODO: Write implementation
        pass

