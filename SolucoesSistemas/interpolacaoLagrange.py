def lagrange_interpolation_polynomial(x_points, y_points):
    """
    Calcula o polinômio interpolador de Lagrange para um conjunto de pontos
    e retorna o polinômio em forma simbólica.
    
    Parâmetros:
    x_points -- lista dos pontos x
    y_points -- lista dos pontos y correspondentes
    
    Retorna:
    Uma função polinomial representando o polinômio interpolador de Lagrange.
    """
    import sympy as sp
    
   
    x = sp.symbols('x')
    
    
    n = len(x_points)
    
    # inicia o polinômio de Lagrange
    polynomial = 0
    
    #polinômio
    for i in range(n):
        
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_points[j]) / (x_points[i] - x_points[j])
        
        # Adiciona o termo L_i(x) * y_i ao polinômio
        polynomial += y_points[i] * L_i
    
    # Simplifica e exibe o polinômio
    polynomial = sp.simplify(polynomial)
    return polynomial

# Pontos de entrada
x_points = [1, 2, 3, 4]
y_points = [5.69, 11.1, 16.39, 21.61]

# Calcula o polinômio interpolador de Lagrange
polynomial = lagrange_interpolation_polynomial(x_points, y_points)
print("Polinômio interpolador de Lagrange:")
print(polynomial)
