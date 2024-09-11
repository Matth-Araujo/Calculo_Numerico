def f(x):
    return (x + 1) * (x - 1) * (x - 3)

def metodo_bisseccao(a, b, e):
    interacao = 0
    if f(a) * f(b) < 0:
        while abs(b - a) > e:
            interacao += 1
            m = (a + b) / 2
            if f(m) == 0:
                print(f"A raiz é = {m}")
                break
            else:
                if f(a) * f(m) < 0:
                    b = m
                else:
                    a = m
        print(f"O valor aproximado da raiz é = {m}")
        print(f"Interações = {interacao}")
    else:
        print("Não existe raiz no intervalo")

intervalos = [(-4, 0), (0, 2), (2, 4)]  # para múltiplas raízes
for a, b in intervalos:
    metodo_bisseccao(a, b, 0.01)
