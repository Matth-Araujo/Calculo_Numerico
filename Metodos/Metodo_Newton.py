def f(x):
    return x**2 - 2

def f_prime(x):
    return 2 * x

def newton(f, f_prime, x0, tol=1e-7, max_iter=1000):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if abs(fpx) < tol:
            print("Derivada próxima de zero. Método falhou.")
            return x, i
        x_new = x - fx / fpx
        if abs(x_new - x) < tol:
            return x_new, i
        x = x_new
    print("Número máximo de iterações alcançado. Método falhou.")
    return x, max_iter

# Usando o método de Newton para encontrar a raiz de f(x)
x0 = 1.0  # Aproximação inicial
raiz, iteracoes = newton(f, f_prime, x0)
print("A raiz encontrada é:", raiz)
print("Número de iterações:", iteracoes)
