import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-10, max_iter=100):
    n = len(b)
    
    # Inicializando x com valores iniciais (se não fornecidos, assume zero)
    x = np.zeros(n) if x0 is None else x0.copy()
    
    # Iteração de Gauss-Seidel
    for k in range(max_iter):
        x_new = x.copy()
        
        for i in range(n):
            # Somatório para a i-ésima linha, usando os valores mais recentes de x
            s = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
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
A = np.array([[2, 1],
              [3, 4]], dtype=float)
b = np.array([1, -1], dtype=float)

x0 = np.zeros(len(b))  # Valor inicial (opcional)

sol = gauss_seidel(A, b, x0=x0, tol=1e-6, max_iter=100)
print("Solução do sistema:", sol)
