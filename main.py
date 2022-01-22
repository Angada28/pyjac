from matrix import *
from complex_number import *
from vector import *


def create_matrix(rows: int, columns: int) -> CoefficientMatrix:
    """Helper function to create a CoefficientMatrix

    pre: 1 <= <rows>, 1 <= <columns>
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


def create_augmented(rows: int, columns: int) -> AugmentedMatrix:
    """Helper function to create a AugmentedMatrix

    pre: 1 <= <rows>, 2 <= <columns>
    post: returns a AugmentedMatrix with <rows> rows and <columns> columns
    """
    _coefficients = []
    _constants = []
    row_i = 0

    while row_i < rows:
        row_str = input('Please input row {}: '.format(row_i + 1)).strip() \
            .split()
        if len(row_str) != columns:
            print('Invalid row input! Please give a correct input ')
        else:
            row = [int(i) for i in row_str]
            _coefficients.append(row[:-1])
            _constants.append(row[-1])
            row_i += 1

    return AugmentedMatrix(CoefficientMatrix(_coefficients), _constants)


def create_vector(lgt: int) -> Vector:
    """Helper function to create a Vector

    pre: 1 <= <len>
    post: returns a Vector with <len> values
    """
    vector = []
    i = 0

    while i < lgt:
        num = input('Input number {}: '.strip().format(i + 1))

        if '.' in num:
            try:
                vector.append(float(num))
            except NameError:
                print("Incorrect value. Please try again.")
                create_vector(lgt)
        else:
            try:
                vector.append(int(num))
            except NameError:
                print("Incorrect value. Please try again.")
                create_vector(lgt)
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
    choices = {1: 'Determinant', 2: 'Cross-product', 3: 'Dot-product',
               4: 'Inverse', 5: 'Gaussian-elimination', 6: 'RREF'}
    operations = {1: 'addition', 2: 'subtraction', 3: 'multiplication',
                  4: 'division'}

    while running:
        print("Please pick one of the following that you would like to "
              "calculate.")
        for key in choices:
            print("{}. {}".format(key, choices[key]))

        choice = input('Input a number between 1 and 6: ')
        while not choice.isnumeric() or 1 > int(choice) > 6:
            print('Invalid input!')
            choice = input('Input a number between 1 and 6: ')

        if choices[int(choice)] == 'Determinant':
            print("We're going to calculate the determinant of a coefficient "
                  "matrix. Let's create the matrix\n")
            m = create_matrix(int(input('How many rows would you like your '
                                        'matrix to have?: ')),
                              int(input('How many columns would you like your '
                                        'matrix to have?: ')))

            print('\n' + str(m.determinant()))

            running = yes_or_no()

        elif choices[int(choice)] == 'Cross-product':
            print("We're going to calculate the cross product of two vectors. "
                  "Let's create the vectors\n")
            length = int(input('How many numbers do you want the vectors to '
                               'have?: '))

            while length < 3:
                print("Vectors must be in R3. Please try again.")
                length = int(input('How many numbers do you want the vectors '
                                   'to have?: '))

            v1 = create_vector(length)
            v2 = create_vector(length)

            print('\nthe cross-product of the two vectors is \n{}'.format(
                v1.cross_product(v2)))

            running = yes_or_no()

        elif choices[int(choice)] == 'Dot-product':
            print(9)
            print("We're going to calculate the dot product of two vectors. "
                  "Let's create the vectors\n")
            length = int(input('How many numbers do you want the vectors to '
                               'have?: '))
            v1 = create_vector(length)
            v2 = create_vector(length)

            print('\nThe dot-product of the two vectors is \n{}'.format(
                v1.dot_product(v2)))

            running = yes_or_no()

        elif choices[int(choice)] == 'Inverse':
            print("We're going to find the inverse of a coefficient "
                  "matrix. Let's create the matrix\n")
            m = create_matrix(int(input('How many rows would you like your '
                                        'matrix to have?: ')),
                              int(input('How many columns would you like your '
                                        'matrix to have?: ')))

            print('\n' + str(m.get_inverse()))
            running = yes_or_no()

        elif choices[int(choice)] == 'Gaussian-elimination':
            print("We're going to find the solutions to an augmented matrix"
                  "in parametric form using Gaussian Elimination.\n")
            m = create_augmented(int(input('How many rows would you like your '
                                           'matrix to have?: ')),
                                 int(input(
                                     'How many columns would you like your '
                                     'matrix to have?: ')))

            print('\n' + str(m.gaussian()))
            running = yes_or_no()

        elif choices[int(choice)] == 'RREF':
            print("We're going to find the RREF of an augmented matrix\n")
            m = create_augmented(int(input('How many rows would you like your '
                                           'matrix to have?: ')),
                                 int(input(
                                     'How many columns would you like your '
                                     'matrix to have?: ')))

            print('\n' + str(m.get_rref()))
            running = yes_or_no()

    print('\nThank you for using our program! Enjoy the rest of your day!')
