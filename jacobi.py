"""
    Este programa resuelve un sistema de ecuaciones lineales por el metodo de Jacobi
"""
import numpy as np


def jacobi(A, b, n, its, tol):

    # Mostrar titulo tabla
    titulo = ' k'
    for i in range(1, n+1):
        titulo = titulo + '   ' + f'x{i}'
    titulo = titulo + '   error'
    print(titulo)

    # inicializar los tres vectores con cero
    v1 = np.zeros(n)
    v2 = np.zeros(n)
    v3 = np.zeros(n)
    divs = np.zeros(n)
    error = 1
    k = 0

    # Mostrar iteracion cero tabla
    if k == 0:
        chain = f' {k}'
        for i in range(n):
            chain = chain + f'   {v1[i]}'
        print(chain)

    while error > tol:
        # Obtener v2
        for i in range(n):
            suma = 0
            for j in range(n):
                if i != j:
                    suma = suma + A[i][j] * v1[j]
                else:
                    divs[i] = A[i][j]
            v2[i] = b[i] - suma

        for i in range(n):
            v2[i] = v2[i] / divs[i]

        # Llenar v3
        for i in range(n):
            v3[i] = v2[i] - v1[i]

        # Encontrar maximo v3
        max1 = abs(v3[0])
        for i in range(1, n):
            if abs(v3[i] >= max1):
                max1 = abs(v3[i])

        # Encontrar maximo vector2
        max2 = abs(v2[0])
        for i in range(1, n):
            if abs(v2[i] >= max2):
                max2 = abs(v2[i])

        # Encontrar error relativo
        error = max1 / max2

        # Mostrar valores tabla
        k += 1
        cadena = f' {k}'
        for i in range(n):
            cadena = cadena + f'   {round(v2[i], 5)}'
        cadena = cadena + f'   {round(error, 5)}'
        print(cadena)
        v1 = v2.copy()

    # Comprobar si el sistema converge o diverge
    if k > its:
        print('El sistema diverge')
    else:
        print('El sistema converge')


# Ingreso de Datos
n = int(input('Ingrese el numero de incognitas: '))
A = np.zeros((n, n))
b = np.zeros(n)

# Ingresar coeficientes
num_ecuacion = 1
for i in range(n):
    print(f"Ingrese los valores de la ecuacion {num_ecuacion}")
    num_coeficiente = 1
    for j in range(n):
        A[i][j] = float(input(f'Ingrese el valor de x{num_coeficiente}:'))
        num_coeficiente += 1
    b[i] = float(input(f'Ingrese el valor de b{num_ecuacion}:'))
    num_ecuacion += 1

# Comprobar que el sistema es estrictamente dominante
# Recorrer matriz A
estado = True
for i in range(n):
    for j in range(n):
        if (abs(A[i][i]) < abs(A[i][j])) or (abs(A[i][i]) < abs(A[j][i])):
            estado = False
            break

if estado:
    its = int(input('Ingrese el numero de iteraciones'))
    tol = float(input('Ingrese el valor de la tolerancia'))
    jacobi(A, b, n, its, tol)
else:
    print('El sistema no es estrictamente dominante')
