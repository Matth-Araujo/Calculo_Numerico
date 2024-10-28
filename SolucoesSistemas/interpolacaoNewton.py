import sympy as sp
def newton_interpolation_polynomial(x_points, y_points):
    """
    Calcula o polinômio interpolador de Newton para um conjunto de pontos
    e retorna o polinômio em forma simbólica.
    
    Parâmetros:
    x_points -- lista dos pontos x
    y_points -- lista dos pontos y correspondentes
    
    Retorna:
    Uma função polinomial representando o polinômio interpolador de Newton.
    """
    
    # Número de pontos
    n = len(x_points)
    
    # Variável simbólica
    x = sp.symbols('x')
    
    # Matriz para armazenar as diferenças divididas
    divided_diff = [[0] * n for _ in range(n)]
    
    # Inicializa a primeira coluna com os valores y
    for i in range(n):
        divided_diff[i][0] = y_points[i]
    
    # Calcula as diferenças divididas
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i][j] = (divided_diff[i+1][j-1] - divided_diff[i][j-1]) / (x_points[i+j] - x_points[i])
    
    # Monta o polinômio de Newton
    polynomial = divided_diff[0][0]
    product = 1
    for i in range(1, n):
        product *= (x - x_points[i-1])
        polynomial += divided_diff[0][i] * product
    
    # Simplifica e exibe o polinômio
    polynomial = sp.simplify(polynomial)
    return polynomial

# Pontos de entrada
x_points = [1.1, 2.2, 3.5]
y_points = [10, 29, 90]

# Calcula o polinômio interpolador de Newton
polynomial = newton_interpolation_polynomial(x_points, y_points)
print("Polinômio interpolador de Newton:")
print(polynomial)
