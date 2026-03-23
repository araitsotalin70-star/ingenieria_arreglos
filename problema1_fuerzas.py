# problema1_fuerzas.py

import numpy as np

# Matriz 3x3 de fuerzas (ejemplo)
fuerzas = np.array([
    [10, -5, 3],
    [4, -8, 6],
    [-7, 2, -5]
])

# Suma total de fuerzas
suma_total = np.sum(fuerzas)

# Reacciones (para equilibrio debe ser 0)
reaccion = -suma_total

print("Matriz de fuerzas:\n", fuerzas)
print("Suma total:", suma_total)
print("Reacción necesaria:", reaccion)