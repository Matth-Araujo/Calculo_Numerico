function f(x)
    return (x+1)*(x-1)*(x-3)
end

a = -4
b = 4
e = 0.01

function metodoBisseccao(a, b, e)
    interacao = 0
    if f(a) * f(b) < 0
        while abs(b - a) > e
            interacao += 1
            global m = (a + b) / 2
            if f(m) == 0
                println("A raiz é = $m")
                break
            else
                if f(a) * f(m) < 0
                    b = m
                else
                    a = m
                end
            end
        end
        println("O valor aproximado da raiz é = ", m)
        println("Interações = ", interacao)
    else
        println("Não existe raiz no intervalo")
    end
end

intervalos = [(-4, 0), (0, 2), (2, 4)] #para multipla raizes
for (a, b) in intervalos
   metodoBisseccao(a, b, 0.01)
end
