import numpy as np

def gauss_jordan(A, b):
    n = len(b)

    #Eliminação
    for i in range(n):
        if A[i,i] == 0:
            for t in range(i+1,n):
                if A[t,i] != 0:
                    #Trocar linha
                    A[[i,t]] = A[[t,i]]
                    b[[i,t]] = b[[t,i]]
                    break
            else:
                raise ValueError("Sistema sem solução única (troca de linha falhou)")

        #Normalizar a linha para que A[i, i] = 1
        b[i] = b[i] / A[i, i]
        A[i, i:] = A[i, i:] / A[i, i]

        #Eliminar elementos acima e abaixo da diagonal principal
        for j in range(n):
            if j != i:
                m = A[j, i]
                A[j, i:] = A[j, i:] - m * A[i, i:]
                b[j] = b[j] - m * b[i]

    return b


A = np.array([[25, 5, 1],
               [64, 8, 1],
               [144, 12, 1]], dtype=float)
b = np.array([106.8, 177.2, 279.2], dtype=float)


x = gauss_jordan(A, b)
print(A)
print(b)
print("Solução do sistema:", x)
