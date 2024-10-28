import numpy as np

def eliminacao_gaussiana(A, b):
    n = len(b)
    
    # Eliminação para triangular a matriz
    for i in range(n):
        # Pivô: Verificação se A[i][i] é zero (para evitar divisão por zero)
        if A[i][i] == 0:
            raise ValueError("Elemento de pivô é zero. Reordene as linhas da matriz.")

        # Normalizando a linha i
        for j in range(i+1, n):
            fator = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= fator * A[i][k]
            b[j] -= fator * b[i]

    # Substituição regressiva para encontrar as soluções
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        soma = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - soma) / A[i][i]
    
    return x

def achar_polinomio_interpolador(x_values, y_values):
    n = len(x_values)
    
    # Construindo a matriz de Vandermonde
    A = np.vander(x_values, N=n, increasing=True).astype(float)
    b = np.array(y_values, dtype=float)
    
    # Resolvendo o sistema com eliminação gaussiana
    coeficientes = eliminacao_gaussiana(A, b)
    
    # Exibindo o polinômio
    print("O polinômio interpolador é:")
    polinomio = "P(x) = "
    for i in range(n):
        if i == 0:
            polinomio += f"{coeficientes[i]:.4f}"
        else:
            polinomio += f" + ({coeficientes[i]:.4f})*x^{i}"
    print(polinomio)
    
    return coeficientes


# Dados da tabela
x_values = [1, 2, 4, 5]
y_values = [12, 4, 8, 9]

# Calculando o polinômio interpolador
coeficientes = achar_polinomio_interpolador(x_values, y_values)
