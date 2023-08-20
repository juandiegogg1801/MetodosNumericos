from math import *
import sympy as sp

def puntoFijo():
    x = sp.symbols('x')
    g = input('Digite la funcion ')
    g = sp.lambdify(x, g)
    x0 = float(input('Digite un valor inicial '))
    n = int(input('Digite las iteraciones a realizar '))
    tol = float(input('Digite el error maximo permitido '))
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


puntoFijo()
