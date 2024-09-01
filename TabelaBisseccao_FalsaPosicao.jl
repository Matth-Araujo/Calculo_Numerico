using Printf

function f(x)
    return x^4/10 - 2*x^2 + -x - 3*sin(x) + 5
end

tol = 0.0001
a = 0.0
b = 2.0

function falsa_posicao(a, b, fa, fb)
    return a - fa * (b - a) / (fb - fa)
end

m = falsa_posicao(a, b, f(a), f(b))

println("\nMétodo da Falsa Posição: \n")
while abs(f(m)) > tol
    @printf("a=%.5f b=%.5f m=%.5f, f(a)=%.5f f(m)=%.5f f(b)=%.5f, (b-a)=%.5f\n", a, b, m, f(a), f(m), f(b), (b - a))

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


function f(x)
  return x^4/10 - 2*x^2 + -x-3*sin(x) + 5
end

m = a + (b - a) / 2

println("\nMétodo de Bissecção: \n")
while abs(f(m)) > tol
  @printf("a=%.5f b=%.5f m=%.5f, f(a)=%.5f f(m)=%.5f f(b)=%.5f, (b-a)=%.5f\n", a, b, m, f(a), f(m), f(b), (b - a))

  if f(a) * f(m) < 0
    global   b = m
  elseif f(b) * f(m) < 0
    global  a = m
  else
      break
  end
    global m = a + (b - a) / 2
end

@printf("\nFinalmente raiz = %.5f\n", m)