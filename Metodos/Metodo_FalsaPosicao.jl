function falsa_posicao(a, b, fa, fb)
    return a - fa * (b - a) / (fb - fa)
end

m = falsa_posicao(a, b, f(a), f(b))

println("\nMétodo da Falsa Posição: \n")
while abs(f(m)) > tol
    if f(a) * f(m) < 0
       global  b = m
    elseif f(b) * f(m) < 0
       global  a = m
    else
        break
    end
   global  m = falsa_posicao(a, b, f(a), f(b))
end

@printf("\nFinalmente raiz = %.5f\n", m)