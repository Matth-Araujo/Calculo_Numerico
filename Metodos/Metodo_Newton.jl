# Definindo a função e sua derivada
f(x) = x^2 - 2
f_prime(x) = 2x

# Implementação do método de Newton
function newton(f, f_prime, x0, tol=1e-7, max_iter=1000)
    x = x0
    for i in 1:max_iter
        fx = f(x)
        fpx = f_prime(x)
        if abs(fpx) < tol
            println("Derivada próxima de zero. Método falhou.")
            return x, i
        end
        x_new = x - fx / fpx
        if abs(x_new - x) < tol
            return x_new, i
        end
        x = x_new
    end
    println("Número máximo de iterações alcançado. Método falhou.")
    return x, max_iter
end

# Usando o método de Newton para encontrar a raiz de f(x)
x0 = 1.0  # Aproximação inicial
raiz, iteracoes = newton(f, f_prime, x0)
println("A raiz encontrada é: ", raiz)
println("Número de iterações: ", iteracoes)
