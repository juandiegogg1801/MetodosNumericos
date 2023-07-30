from math import *


def f(x):
    return x ** 3 + 2 * pow(x, 2) + 10 * x - 20


def secante(x1, x2, tol):
    error = 1
    n = 1
    x3 = 0
    dx = 0
    print('  i          X0             Xi             Xi+1       |Xi-1 - Xi|       Error')
    while error > tol:
        x3 = x1 - ((x2 - x1) / (f(x2) - f(x1))) * f(x1)
        error = abs((x2 - x1) / x2)
        dx = abs(x1 - x2)
        if n == 1:
            print(' ', n, '      ', round(x1, 5), '               ', round(x2, 5), '         ', round(x3, 5), '         ',
                  round(dx, 5),
                  '           ', round(error, 5))
        elif n == 2:
            print(' ', n, '      ', round(x1, 5), '            ', round(x2, 5), '      ', round(x3, 5), '      ',
                  round(dx, 5),
                  '      ', round(error, 5))
        else:
            print(' ', n, '      ', round(x1, 5), '      ', round(x2, 5), '      ', round(x3, 5), '      ',
                  round(dx, 5),
                  '      ', round(error, 5))
        x1 = x2
        x2 = x3
        n += 1
    if error < tol:
        print('x', n - 1, '=', round(x2, 5), end=' ')
        print('es una buena aproximacion de la raiz')
        return


secante(0, 1, 0.001)
