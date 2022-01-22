from matrix import *
from complex_number import *
from vector import *
from linear_algebra_algorithms import *


def create_matrix(rows: int, columns: int) -> CoefficientMatrix:
    """Helper function to create a CoefficientMatrix

    pre: 1 <= <rows>, <columns>
    post: returns a CoefficientMatrix with <rows> rows and <columns> columns
    """
    matrix = []
    row_i = 0

    while row_i < rows:
        row_str = input('Please input row {}: '.format(row_i + 1)).strip() \
            .split()
        if len(row_str) != columns:
            print('Invalid row input! Please give a correct input ')
        else:
            row = [int(i) for i in row_str]
            matrix.append(row)
            row_i += 1

    return CoefficientMatrix(matrix)


def create_vector(lgt: int) -> Vector:
    """Helper function to create a Vector

    pre: 1 <= <len>
    post: returns a Vector with <len> values
    """
    vector = []
    i = 0

    while i < lgt:
        num = input('Input number {}'.strip().format(i + 1))
        if '.' in num:
            vector.append(float(num))
        else:
            vector.append(int(num))
        i += 1

    return Vector(vector)


def yes_or_no() -> bool:
    """Returns True iff <response> == 'yes'. Returns False iff <response> ==
    'no'

    pre: <response> is either 'yes' or 'no'
    """
    cont = input('Would you like to continue?[yes/no]?: ')
    if cont.lower() != 'no' and cont.lower() != 'yes':
        while cont.lower() != 'no' and cont.lower() != 'yes':
            cont = input('Invalid response. Please try again[yes/no]: ')

    if cont == 'yes':
        return True
    return False


if __name__ == '__main__':
    running = True
    choices = {1: 'determinant', 2: 'cross-product', 3: 'dot-product',
               4: 'inverse', 5: 'gaussian-elimination', 6: 'rref'}
    operations = {1: 'addition', 2: 'subtraction', 3: 'multiplication',
                  4: 'division'}

    while running:
        choice = input('input a number between 1 and 6: ')
        if not choice.isnumeric() or 1 > int(choice) > 6:
            print('Invalid input!')
        elif choices[int(choice)] == 'determinant':
            print("We're going to calculate the determinant of a coefficient "
                  "matrix. Let's create the matrix\n")
            m = create_matrix(int(input('how many rows would you like your '
                                        'matrix to have?: ')),
                              int(input('how many columns would you like your '
                                        'matrix to have?: ')))

            print('\n' + str(determinant(m)))

            running = yes_or_no()
        elif choices[int(choice)] == 'cross-product':
            print("We're going to calculate the cross product of two vectors. "
                  "Let's create the vectors\n")
            length = int(input('How many numbers do you want the vectors to '
                               'have?: '))
            v1 = create_vector(length)
            v2 = create_vector(length)

            print('\nthe cross-product of the two vectors is \n{}'.format(
                cross_product(v1, v2)))

            running = yes_or_no()
        elif choices[int(choice)] == 'dot-product':
            print("We're going to calculate the dot product of two vectors. "
                  "Let's create the vectors\n")
            length = int(input('How many numbers do you want the vectors to '
                               'have?: '))
            v1 = create_vector(length)
            v2 = create_vector(length)

            print('\nthe dot-product of the two vectors is \n{}'.format(
                dot_product(v1, v2)))

            running = yes_or_no()
        elif choices[int(choice)] == 'inverse':
            print("We're going to find the inverse of a coefficient "
                  "matrix. Let's create the matrix\n")
            m = create_matrix(int(input('how many rows would you like your '
                                        'matrix to have?: ')),
                              int(input('how many columns would you like your '
                                        'matrix to have?: ')))

            print('\n' + str(get_inverse(m)))
        elif choices[int(choice)] == 'gaussian-elimination':
            pass
        else:
            pass

    print('Thank you for using our program! Enjoy the rest of your day!')
