from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """function: calculate_square_root."""
    if your_number >= 0:
        print(f'Мы вычислили квадратный корень из введённого вами числа. '
              f'Это будет: {calculate_square_root(your_number)}')


print(message)
calc(25.5)
