dirfrom math import *


def g(x):
    return ((4 - 1/(2*x) - (2*x**2)/7)**2) ** (1/3)


def puntoFijo(x0, n, tol):
    print('  i      Xi        error')
    print('  0     ', x0)
    for i in range(n):
        x = g(x0)
        error = abs((x - x0) / x)
        if error < tol:
            print(' ', i + 1, '  ', round(x, 5), '  ', round(error, 5), ' es un punto fijo')
            return x
        x0 = x
        print(' ', i + 1, '  ', round(x, 5), '  ', round(error, 5), )


result = puntoFijo(1.5, 20, 0.0001)
