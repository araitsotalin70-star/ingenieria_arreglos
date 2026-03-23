# problema2_fluido.py

import numpy as np

# Fluido 3D (presión inicial)
fluido = np.random.rand(3,3,3)

def actualizar(f):
    nuevo = np.copy(f)
    
    for i in range(1,2):
        for j in range(1,2):
            for k in range(1,2):
                vecinos = [
                    f[i+1][j][k], f[i-1][j][k],
                    f[i][j+1][k], f[i][j-1][k],
                    f[i][j][k+1], f[i][j][k-1]
                ]
                nuevo[i][j][k] = sum(vecinos)/6
    
    return nuevo

print("Antes:\n", fluido)
fluido = actualizar(fluido)
print("Después:\n", fluido)