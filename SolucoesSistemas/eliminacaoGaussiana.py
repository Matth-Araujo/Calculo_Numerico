import numpy as np

def eliminacao_gaussiana(A, b):
    n = len(b)

    # Eliminação
    for i in range(n-1):
        if A[i,i] == 0:
            for t in range(i+1,n):
                if A[t,i] != 0:
                    # Trocar linha
                    A[[i,t]] = A[[t,i]]
                    b[[i,t]] = b[[t,i]]
                    break
            else:
                raise ValueError("Sistema sem solução única (troca de linha falhou)")
            
        # Prosseguir com a eliminação   
        for j in range(i+1, n):
            m = A[j, i] / A[i, i]
            A[j, i:] = A[j, i:] - m * A[i, i:]
            b[j] = b[j] - m * b[i]
               
    # Solução do sistema por substituição retroativa
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1,n-1]

    for i in range(n-2,-1,-1):
        x[i] = b[i]
        for j in range(i+1,n):
            x[i] = x[i] - A[i,j] * x[j]
        x[i] = x[i] / A[i,i]

    return x

# Imprimir matriz A e vetor b antes da eliminação
A = np.array([[1, 2],
              [-1, 1]], dtype=float)

b = np.array([7, 8], dtype=float)

# Resolver o sistema usando eliminação gaussiana
x = eliminacao_gaussiana(A, b)

print("Solução do sistema 59):", x)


A1 = np.array([[2, 6],
              [2, 3]],dtype=float)
b1 = np.array([16, 7],dtype=float)

x1 = eliminacao_gaussiana(A1, b1)
print("Solução do sistema 60):", x1)


A2 = np.array([[3, -2],
              [1, 3]],dtype=float)
b2 = np.array([-27, 13],dtype=float)

x2 = eliminacao_gaussiana(A2, b2)
print("Solução do sistema 61):", x2)

A3 = np.array([[-1, 1],
              [2, -4]],dtype=float)
b3 = np.array([4, -34],dtype=float)

x3 = eliminacao_gaussiana(A3, b3)
print("Solução do sistema 62):", x3)

A4 = np.array([[1, 2, -3],
              [0, 4, 2],
              [-1, 1, -1]],dtype=float)
b4 = np.array([-28, 0,-5],dtype=float)

x4 = eliminacao_gaussiana(A4, b4)
print("Solução do sistema 63):", x4)

A5 = np.array([[3, -2, 1],
              [-1, 1, 2],
              [1, -1, -4]],dtype=float)
b5 = np.array([15, -10,14],dtype=float)

x5 = eliminacao_gaussiana(A5, b5)
print("Solução do sistema 64):", x5)

print("65) sem solução")

print("66) sem solução")

A6 = np.array([[3, 2, -1, 1],
              [1, -1, 4, 2],
              [-2, 1, 2, -1],
              [1, 1, 1, 1]],dtype=float)
b6 = np.array([0, 25, 2, 6],dtype=float)

x6 = eliminacao_gaussiana(A6, b6)
x6 = np.round(x6, decimals=10)  # Arredonda para 10 casas decimais
print("Solução do sistema 67):", x6)

A7 = np.array([[1, -4, 3, -2],
              [3, -2, 1, -4],
              [-4, 3, -2, 1],
              [-2, 1, -4, 3]],dtype=float)
b7 = np.array([9, -13, -4, -10],dtype=float)

x7 = eliminacao_gaussiana(A7, b7)
x7 = np.round(x7, decimals=10)
print("Solução do sistema 68):", x7)
