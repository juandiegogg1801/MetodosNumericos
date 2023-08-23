"""
    Este programa resuelve un sistema de ecuaciones lineales por el metodo de Gauss-Seidel
"""

def X1(x2):
    x1 = (x2 / 4) + 1 / 4
    return x1


def X2(x1, x3):
    x2 = (x1 / 4) + (x3 / 4) + 1 / 4
    return x2


def X3(x2, x4):
    x3 = (x2 / 4) + (x4 / 4) + 1 / 4
    return x3


def X4(x3):
    x4 = (x3 / 4) + 1 / 4
    return x4


def gaussSeidel(n, iteraciones, tol):
    print('  k        X1       X2        X3        X4')
    vector1 = []
    vector2 = []
    vector3 = []

    for i in range(n):
        vector1.append(0)
    for i in range(n):
        vector2.append(0)
    for i in range(n):
        vector3.append(0)

    error = 1
    k = 0
    while error > tol and k < iteraciones:
        max1 = 0
        max2 = 0

        x1 = vector1[0]
        x2 = vector1[1]
        x3 = vector1[2]
        x4 = vector1[3]

        print(' ', k, '   ', round(x1, 5), '   ', round(x2, 5), '   ', round(x3, 5), '   ', round(x4, 5))

        vector2[0] = X1(x2)
        x1 = vector2[0]
        vector2[1] = X2(x1, x3)
        x2 = vector2[1]
        vector2[2] = X3(x2, x4)
        x3 = vector2[2]
        vector2[3] = X4(x3)
        x4 = vector2[3]

        vector3[0] = vector2[0] - vector1[0]
        vector3[1] = vector2[1] - vector1[1]
        vector3[2] = vector2[2] - vector1[2]
        vector3[3] = vector2[3] - vector1[3]

        if abs(vector3[0]) >= abs(vector3[1]) and abs(vector3[0]) >= abs(vector3[2]) and abs(vector3[0]) >= abs(
                vector3[3]):
            max1 = vector3[0]
        elif abs(vector3[1]) >= abs(vector3[0]) and abs(vector3[1]) >= abs(vector3[2]) and abs(vector3[1]) >= abs(
                vector3[3]):
            max1 = vector3[1]
        elif abs(vector3[2]) >= abs(vector3[0]) and abs(vector3[2]) >= abs(vector3[1]) and abs(vector3[2]) >= abs(
                vector3[3]):
            max1 = vector3[2]
        else:
            max1 = vector3[3]

        if abs(vector2[0]) >= abs(vector2[1]) and abs(vector2[0]) >= abs(vector2[2]) and abs(vector2[0]) >= abs(
                vector2[3]):
            max2 = vector2[0]
        elif abs(vector2[1]) >= abs(vector2[0]) and abs(vector2[1]) >= abs(vector2[2]) and abs(vector2[1]) >= abs(
                vector2[3]):
            max2 = vector2[1]
        elif abs(vector2[2]) >= abs(vector2[0]) and abs(vector2[2]) >= abs(vector2[1]) and abs(vector2[2]) >= abs(
                vector2[3]):
            max2 = vector2[2]
        else:
            max2 = vector2[3]
        error = max1 / max2
        vector1 = vector2.copy()
        k += 1
    if k > iteraciones:
        print('El sistema de ecuaciones diverge')
    else:
        print('El sistema de ecuaciones converge')


n = int(input('Ingrese el numero de incognitas'))
iteraciones = int(input('Ingrese el numero de iteraciones'))
gaussSeidel(n, iteraciones, 0.00001)