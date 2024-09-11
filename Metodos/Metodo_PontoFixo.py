def ponto_fixo(g, x0, erro=1e-5, iteracao=100):
    x = x0
    for i in range(iteracao):
        x_novo = g(x)
        if abs(x_novo - x) < erro:
            return x_novo, i
        x = x_novo
    raise ValueError(f"O método não convergiu em {iteracao} iterações")

def g(x):
    return (x + 1)**(1/3)

x0 = 1

raiz, iteracoes = ponto_fixo(g, x0)
print("Raiz encontrada:", raiz)
print("Número de iterações:", iteracoes)
