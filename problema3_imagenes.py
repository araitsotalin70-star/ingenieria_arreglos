# problema3_imagenes.py

import numpy as np

volumen = np.random.randint(0, 255, (3,3,3))

def suavizar(v):
    nuevo = np.copy(v)
    
    for i in range(1,2):
        for j in range(1,2):
            for k in range(1,2):
                vecinos = v[i-1:i+2, j-1:j+2, k-1:k+2]
                nuevo[i][j][k] = np.mean(vecinos)
    
    return nuevo

print("Original:\n", volumen)
print("Suavizado:\n", suavizar(volumen))