import numpy as np

def decomposicao_LU(A):
    n = A.shape[0]
    L = np.zeros_like(A)
    U = np.zeros_like(A)

    # Itera para construir L e U
    for i in range(n):
        # Construção da matriz U
        for k in range(i, n):
            soma = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - soma

        # Construção da matriz L
        for k in range(i, n):
            if i == k:
                L[i][i] = 1  # Diagonal principal de L é 1
            else:
                soma = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - soma) / U[i][i]

    return L, U
# Definindo a matriz A e o vetor b
A = np.array([[3, 2, 4],
              [1, 1, 2],
              [4, 3, -2]], dtype=float)
b = np.array([1, 2, 4], dtype=float)

# Realizando a decomposição LU
L, U = decomposicao_LU(A)
print("Matriz L:")
print(L)
print("Matriz U:")
print(U)

# Passo 1: Resolva Ly = b
y = np.linalg.solve(L, b)
# Passo 2: Resolva Ux = y
x = np.linalg.solve(U, y)

print("Solução do sistema Ax = b:")
print(x)
