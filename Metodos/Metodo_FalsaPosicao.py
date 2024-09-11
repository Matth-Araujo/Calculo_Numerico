def f(x):
    return (x + 1) * (x - 1) * (x - 3)

def falsa_posicao(a, b, fa, fb):
    return (a*f(b) - b*f(a))/(f(b)-f(a))

a = -4
b = 4
tol = 0.01

m = falsa_posicao(a, b, f(a), f(b))

print("\nMétodo da Falsa Posição: \n")
while abs(f(m)) > tol:
    if f(a) * f(m) < 0:
        b = m
    elif f(b) * f(m) < 0:
        a = m
    else:
        break
    m = falsa_posicao(a, b, f(a), f(b))

print(f"\nFinalmente raiz = {m:.5f}\n")
