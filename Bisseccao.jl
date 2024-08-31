function metodoBisseccao(a,b,e)
    interacao = 0
    if f(a) * f(b) < 0
        while (abs( (b - a)/2 ) > e)
            interacao += 1
            global m = (a + b) / 2
            if (f(m) == 0)
                println("A raiz é = $m")
                break
            else
                if f(a) * f(m) < 0
                 b = m
                else
                 a = m
                 #println("O valor aproximado é $m")
                end
            end
        end
        println("O valor aproximado da raiz é = ", m)
        println("Interação: $interacao")
    else
        println("Não existe raiz no intervalo")
    end
    
end


println("Questao 2.1:")
function f(x)
    return x^2 -5
end
metodoBisseccao(0,1,0.01)


println("Questao 2.2:")
function f(x)
    return x^2 -5
end
metodoBisseccao(2.2303 , 6 ,0.01)


println("Questao 2.3.1:")
function f(x)
    return 2*x^3 - x^2 + x - 1
end
metodoBisseccao( -4, 4 ,0.01)

println("Questao 2.3.2:")
function f(x)
    return 2*x^3 - x^2 + x - 1
end
metodoBisseccao( 0, 1 ,0.01)

println("Questao 2.4:")
function f(x)
    return x^3 + 4*x^2 - 10 
end
metodoBisseccao( 1, 2 ,10^(-5))
println()

# com for
println("Questao 2.5")

function metodoBisseccao(a, b, e)
    interacao = 0
    max_iteracoes = ceil(Int, log((b - a) / e)/log(2.0))  

    if f(a) * f(b) < 0
        for i in 1:max_iteracoes
            interacao += 1
            m = (a + b) / 2
            if f(m) == 0
                println("A raiz é = $m")
                break
            else
                if f(a) * f(m) < 0
                    b = m
                else
                    a = m
                end
                # println("O valor aproximado é $m")
            end
            if abs((b - a) / 2) <= e
                break
            end
        end
        println("O valor aproximado da raiz é = $m")
        println("Interação: $interacao")
    else
        println("Não existe raiz no intervalo")
    end
end
