using Printf  #Para a função @printf

function f(x)
    return x^2 - 8  # Defino a função f(x) = x^2 - 8
end

function bissecao(f, a, b, e)
    fa = f(a)  #Calculando o valor de f(a)
    if fa == 0.0
        return a  #Se f(a) é 0, 'a' é a raiz, então retorna 'a'
    end
    
    fb = f(b)  #Calculando o valor de f(b)
    if fb == 0.0
        return b  #Se f(b) é 0, 'b' é a raiz, então retorna 'b'
    end
    
    if fa * fb < 0.0  # Se f(a) e f(b) têm sinais opostos, existe uma raiz no intervalo [a, b]
        n = ceil(log(abs(b - a) / e) / log(2.0))  #Calculando o número máximo de iterações necessárias, com base na precisão 'e'
        
        for i in 1:n
            m = 0.5 * (a + b)  #Calculando o ponto médio do intervalo
            fm = f(m)  #Calculando o valor de f(m)
            
            if fm == 0.0
                return m  #Se f(m) é 0, 'm' é a raiz , então retorna 'm'
            end
            
            if fb * fm < 0.0
                # Se f(m) e f(b) têm sinais opostos, a raiz está no intervalo [m, b]
                a = m  # Atualizando 'a' para 'm'
                fa = fm  # Atualizando f(a) para f(m)
            else
                # Caso contrário, a raiz está no intervalo [a, m]
                b = m  # Atualizando 'b' para 'm'
                fb = fm  # Atualizando f(b) para f(m)
            end
        end
        
        return (a + b) / 2.0  # Retorna a aproximação da raiz após as iterações
    else
        @printf "Não existe raiz no intervalo\n"  # Se f(a) e f(b) têm o mesmo sinal, não há raiz no intervalo [a, b]
        return nothing  # Retorna nothing indicando que não foi encontrada uma raiz
    end
end

