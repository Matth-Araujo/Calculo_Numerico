using Plots


function f(x)
    return x^2 - 8x
end

function grafico(a, b)
    vetor_x = range(a-2, stop=b+2, length=100)
    vetor_y = f.(vetor_x)
    plot(vetor_x, vetor_y, color=:red, label="", grid=true)

    xline = [a, b]
    yline = [f(a), f(b)]
    plot!(xline, yline, marker=:circle, label="")

    xlims!(a-1, b+1)
    ylims!(f(a)-10, f(b)+10)
    title!("função  x^2 - 8 x em [$a,$b]")
    xlabel!("eixo x")
    ylabel!("eixo y")
end


a = 5
b = 12
grafico(a, b)
