import math
from math import *


def f(x):
    return (pow(math.e, x)/2) + (pow(x, 2)/3) - (1/pow(x, 3)) - 2


def biseccion(a, b, tol):
    xi = a
    xr = b
    i = 1
    error = 0
    print('   i      Xr        Xi      Xu      f(Xi)      f(Xr)      e')
    if f(a) * f(b) > 0:
        print('La funcion no cambia de signo')
    while abs(xi - xr) > tol:
        xi = xr
        xr = (a + b) / 2
        if i > 1:
            error = abs((xr - xi) / xr)
        print('  ', i, '   ', round(xr, 5), '     ', round(a, 5),
              '    ', round(b, 5), '   ', round(f(a), 5), '    ',
              round(f(xr), 5), '      ', round(error, 5))

        if f(a) * f(xr) < 0:
            b = xr
        if f(xr) * f(b) < 0:
            a = xr

        i = i + 1
    print('x', i-1, '=', round(xr, 5), ' es una buena aproximacion')


biseccion(1, 2, 10 ** (-2))
