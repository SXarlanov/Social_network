from math import sqrt


message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(Numb):
    """Вычисляет квадратный корень."""
    return sqrt(Numb)


def calc(your_number):
    if your_number <= 0:
        return
    root = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {root}')


calc(25.5)
