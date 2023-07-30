from math import *
from mpmath import cot


def f(x):
    return x ** 3 + 2 * pow(x, 2) + 10 * x - 20


def df(x):
    return 3 * pow(x, 2) + 4 * x + 10


def g(x):
    return x - f(x) / df(x)


def dg(x):
    return abs((6 * pow(x, 4) + 16 * pow(x, 3) + 68 * pow(x, 2) - 80 * x - 80) / pow(3 * pow(x, 2) + 4 * x + 10, 2))


def NewtonRaphson(x0, tol, n):
    error = 0
    print("   i       Xi               Xi+1              e              g'(x)")
    for i in range(n):
        i = i + 1
        x1 = g(x0)
        if i < 2:
            print('  ', i, '   ', round(x0, 5), '              ', round(x1, 5),
                  '        ', round(error, 5), '              ', round(dg(x0), 5))
        else:
            error = abs((x1 - x0) / x1)
            print('  ', i, '   ', round(x0, 5), '        ', round(x1, 5),
                  '        ', round(error, 5), '        ', round(dg(x0), 5))
            if abs(x1 - x0) < tol:
                print('x', i + 1, '=', round(x1, 5), end=' ')
                print('es una buena aproximacion de la raiz')
                return
        x0 = x1


NewtonRaphson(1, 0.001, 5)
