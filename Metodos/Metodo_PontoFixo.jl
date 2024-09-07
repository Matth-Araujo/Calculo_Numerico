function Ponto_Fixo(g,x0;erro= 1e-5,iteracao = 100)
    x = x0
    for i in 1:iteracao
        x_novo = g(x)
        if abs(x_novo - x) < erro
            return x_novo, i            
        end 
        x = x_novo 
    end
    error("O método não convergiu em $iteracao iterações")
end

g(x) = (x+1)^(1/3)

x0 = 1

raiz, iteracoes = Ponto_Fixo(g, x0)
println("Raiz encontrada: ", raiz)
println("Número de iterações: ", iteracoes)