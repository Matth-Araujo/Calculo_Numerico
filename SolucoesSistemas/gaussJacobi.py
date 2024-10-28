import numpy as np

def gauss_jacobi(A, b, x0=None, tol=1e-10, max_iter=100):
    n = len(b)
    
    # Inicializando x com valores iniciais (se não fornecidos, assume zero)
    x = np.zeros(n) if x0 is None else x0.copy()
    
    # Iteração de Jacobi
    for k in range(max_iter):
        x_new = np.zeros(n)
        
        for i in range(n):
            # Somatório para a i-ésima linha, excluindo o termo diagonal
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]
        
        # Mostrar a iteração atual e o valor de x_new
        print(f"Iteração {k + 1}: x = {x_new}")
        
        # Critério de parada baseado na tolerância
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        
        x = x_new
    
    # Se não convergir dentro do número máximo de iterações, retorna o último valor calculado
    print("Atenção: o método não convergiu.")
    return x

# Exemplo de uso
A = np.array([[25, 5, 1],
               [64, 8, 1],
               [144, 12, 1]], dtype=float)
b = np.array([106.8, 177.2, 279.2], dtype=float)

x0 = np.zeros(len(b))  # Valor inicial (opcional)

sol = gauss_jacobi(A, b, x0=x0, tol=1e-6, max_iter=100)
print("Solução do sistema:", sol)
