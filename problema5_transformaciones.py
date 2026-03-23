# problema5_transformaciones.py

import numpy as np
import matplotlib.pyplot as plt

# Puntos
puntos = np.array([
    [1,1],
    [2,1],
    [2,2],
    [1,2]
])

# Rotación 90 grados
theta = np.radians(90)
rotacion = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

# Transformación
transformados = puntos.dot(rotacion)

# Gráfica
plt.scatter(puntos[:,0], puntos[:,1], label="Original")
plt.scatter(transformados[:,0], transformados[:,1], label="Rotado")

plt.legend()
plt.grid()
plt.title("Transformación de puntos")
plt.show()