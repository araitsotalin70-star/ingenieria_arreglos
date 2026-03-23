# problema4_sensores.py

import numpy as np

datos = np.random.randint(20, 35, (5,5))

# Promedios
prom_filas = np.mean(datos, axis=1)
prom_columnas = np.mean(datos, axis=0)

# Desviación estándar
std_filas = np.std(datos, axis=1)
std_columnas = np.std(datos, axis=0)

print("Datos:\n", datos)
print("Promedio filas:", prom_filas)
print("Promedio columnas:", prom_columnas)
print("Desv filas:", std_filas)
print("Desv columnas:", std_columnas)