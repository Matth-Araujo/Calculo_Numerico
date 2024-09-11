using Printf

# Definindo a função
function f(x)
    return (x + 1) * (x - 1) * (x - 3)
end

# Definindo a função de falsa posição
function falsa_posicao(a, b)
    return (a * f(b) - b * f(a)) / (f(b) - f(a))
end

# Definindo os valores iniciais
a = -4
b = 4
tol = 0.01

# Calculando a primeira aproximação
m = falsa_posicao(a, b)

println("\nMétodo da Falsa Posição: \n")
while abs(f(m)) > tol
    if f(a) * f(m) < 0
       global b = m
    elseif f(b) * f(m) < 0
       global a = m
    else
        break
    end
   global m = falsa_posicao(a, b)
end

@printf("\nFinalmente raiz = %.5f\n", m)
