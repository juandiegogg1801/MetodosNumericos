import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# INGRESO
x = sp.symbols('x')

fx = (1 / sp.sqrt(2 * sp.pi)) * sp.exp(-x**2 / 2)

# intervalo de integración
a = -1
b = 1
tramos = 2

# PROCEDIMIENTO
# Regla de Simpson
# Usando tramos equidistantes en intervalo
h = (b-a)/tramos
xi = a
suma = fx.subs(x, xi)
for i in range(1, tramos, 2):  # Solo sumar los términos impares
    xi = a + i*h
    suma = suma + 4*fx.subs(x, xi)
for i in range(2, tramos-1, 2):  # Sumar los términos pares
    xi = a + i*h
    suma = suma + 2*fx.subs(x, xi)
suma = suma + fx.subs(x, b)
area_aproximada = h*(suma/3)

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
plt.title('Integral: Regla de Simpson')
plt.legend()

# Área bajo la curva usando el método de Simpson
x_simpson = np.linspace(a, b, muestraslinea)
fx_simpson = [float(fx.subs(x, val).evalf()) for val in x_simpson]
plt.fill_between(x_simpson, 0, fx_simpson, color='g', alpha=0.3)

plt.show()
