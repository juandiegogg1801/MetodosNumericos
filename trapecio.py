import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# INGRESO
x = sp.symbols('x')

fx = (1 / sp.sqrt(2 * sp.pi)) * sp.exp(-x**2 / 2)

# intervalo de integración
a = -1
b = 1
tramos = 1

# PROCEDIMIENTO
# Regla del Trapecio
# Usando tramos equidistantes en intervalo
h = (b-a)/tramos
xi = a
suma = fx.subs(x, xi)
for i in range(0, tramos-1, 1):
    xi = xi + h
    suma = suma + 2*fx.subs(x, xi)
suma = suma + fx.subs(x, b)
area_aproximada = h*(suma/2)

# Integral exacta
integral_exacta = sp.integrate(fx, (x, a, b))

# Cálculo del error
error = abs(area_aproximada - integral_exacta) / integral_exacta

# SALIDA
print('tramos: ', tramos)
print('Integral aproximada: ', area_aproximada.evalf())
print('Integral exacta: ', integral_exacta.evalf())
print('Error relativo: ', error.evalf())

# GRAFICA
# Puntos de muestra
muestras = tramos + 1
xi = np.linspace(a, b, muestras)
fi = [float(fx.subs(x, val).evalf()) for val in xi]  # Convertir a tipo float
# Linea suave
muestraslinea = tramos*10 + 1
xk = np.linspace(a, b, muestraslinea)
fk = [float(fx.subs(x, val).evalf()) for val in xk]  # Convertir a tipo float

# Graficando
plt.plot(xk, fk, label='f(x)')
plt.plot(xi, fi, marker='o',
         color='orange', label='muestras')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Integral: Regla de Trapecios')
plt.legend()

# Trapecios
plt.fill_between(xi, 0, fi, color='g')
for i in range(0, muestras, 1):
    plt.axvline(xi[i], color='w')

plt.show()
