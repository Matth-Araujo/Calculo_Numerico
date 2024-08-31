function erro_absoluto(x, valorAproximado)
    return abs(x - valorAproximado)
end

function erro_relativo(x, valorAproximado)
    erro = erro_absoluto(x, valorAproximado)
    return erro / abs(valorAproximado)
end

function printValor(vAbsoluto, vRelativo)
    println("Erro Absoluto : $(round(vAbsoluto, digits=8))")
    println("Erro Relativo : $(round(vRelativo, digits=8))\n")
end


pi = 3.141592
e = 2.718282


println("Questao 1:")
println("a)")
a_erroAbsoluto = erro_absoluto(231.29, 232.04)
a_erroRelativo = erro_relativo(231.29, 232.04)
printValor(a_erroAbsoluto, a_erroRelativo)

println("b)")
b_erroAbsoluto = erro_absoluto(0.5682, 0.5701)
b_erroRelativo = erro_relativo(0.5682, 0.5701)
printValor(b_erroAbsoluto, b_erroRelativo)

println("c)")
c_erroAbsoluto = erro_absoluto(12.329, 12.331)
c_erroRelativo = erro_relativo(12.329, 12.331)
printValor(c_erroAbsoluto, c_erroRelativo)


println("Questao 1.1:")

println("a)")
a_erroAbsoluto = erro_absoluto(pi, 22/7)
a_erroRelativo = erro_relativo(pi, 22/7)
printValor(a_erroAbsoluto, a_erroRelativo)

println("b)")
b_erroAbsoluto = erro_absoluto(pi, 3.1416)
b_erroRelativo = erro_relativo(pi, 3.1416)
printValor(b_erroAbsoluto, b_erroRelativo)

println("c)")
c_erroAbsoluto = erro_absoluto(e, 2.718)
c_erroRelativo = erro_relativo(e, 2.718)
printValor(c_erroAbsoluto, c_erroRelativo)

println("d)")
d_erroAbsoluto = erro_absoluto(sqrt(2), 1.414)
d_erroRelativo = erro_relativo(sqrt(2), 1.414)
printValor(d_erroAbsoluto, d_erroRelativo)


println("Questao 1.2:")
println("a)")
a_erroAbsoluto = erro_absoluto(e^10, 22000)
a_erroRelativo = erro_relativo(e^10, 22000)
printValor(a_erroAbsoluto, a_erroRelativo)

println("b)")
b_erroAbsoluto = erro_absoluto(10^pi, 1400)
b_erroRelativo = erro_relativo(10^pi, 1400)
printValor(b_erroAbsoluto, b_erroRelativo)

println("c)")
c_erroAbsoluto = erro_absoluto(factorial(8), 39900)
c_erroRelativo = erro_relativo(factorial(8), 39900)
printValor(c_erroAbsoluto, c_erroRelativo)

println("d)")
d_erroAbsoluto = erro_absoluto(factorial(9), sqrt(18*pi)*(9/e)^9)
d_erroRelativo = erro_relativo(factorial(9), sqrt(18*pi)*(9/e)^9)
printValor(d_erroAbsoluto, d_erroRelativo)


println("Questao 1.3:")
println()

function calcular_intervalo(p)
    erro_relativo = 0.001
    p_min = (1 - erro_relativo) * p
    p_max = (1 + erro_relativo) * p
    return p_min, p_max
end

valores_p = [150, 900, 1500, 90]

for p in valores_p
    p_min, p_max = calcular_intervalo(p)
    println("Para p = $p, p* deve estar no intervalo [$(round(p_min, digits=2)), $(round(p_max, digits=2))]")
    println()
end


println()
println("Questao 1.4:")
println()

using Printf

p_values = Dict(
    "pi" => pi,
    "e" => e,
    "sqrt(2)" => sqrt(2),
    "cbrt(7)" => cbrt(7)
)

erroRelativo = 10^-4

for (nome, p) in p_values
    intervalo_inferior = p * (1 - erroRelativo)
    intervalo_superior = p * (1 + erroRelativo)
    println("Para $nome = $(Printf.@sprintf("%.8f", p)): ")
    println("  Intervalo: [$(Printf.@sprintf("%.8f", intervalo_inferior)), $(Printf.@sprintf("%.8f", intervalo_superior))]")
    println("  Erro relativo máximo: $erroRelativo")
    println()
end
