import numpy as np

Matriz = []
cont = 32
for fila in range(4):
    Matriz.append([])
    for columna in range(8):
        Matriz[fila].append(columna)
        Matriz[fila][columna] = cont
        cont = cont - 1
print(Matriz[0][0])
