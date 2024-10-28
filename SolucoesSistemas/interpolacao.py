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
