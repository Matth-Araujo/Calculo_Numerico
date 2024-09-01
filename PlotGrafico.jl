using Plots

function plot_function(a, b, funcao, f)
    xp = range(a, stop=b, length=100)
    yp = f.(xp)

    plt = plot(xp, yp, label="função $funcao", xlabel="eixo x", ylabel="eixo y", title="função $funcao", grid=:true)
    display(plt)
end

function f1(x)
    return x^2 - x - 1
end
plot_function(-2, 2, "x^2 - x - 1", f1)

function f2(x)
    return x^3 - 3 * sin(x)
end
plot_function(-2, 2, "x^3 - 3 * sin(x)", f2)

function f3(x)
    return exp(x) - 2
end
plot_function(-2, 2, "exp(x) - 2", f3)

function f4(x)
    return sin(50 / (1 + x^2)) + 1 - x^2
end
plot_function(-2, 2, "sin(50 / (1 + x^2)) + 1 - x^2", f4)
