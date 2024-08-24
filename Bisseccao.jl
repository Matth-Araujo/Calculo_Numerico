function f(x)
    return 2*x^3 - x^2 + x -1
end

a = -4
b = 4
e = 0.01

if f(a) * f(b) < 0
    while (abs( (b - a)/2 ) > e)
        global m = (a + b) / 2
        if (f(m) == 0)
            println("A raiz é = $m")
            break
        else
            if f(a) * f(m) < 0
             global b = m
            else
             global a = m
             println("O valor aproximado é $m")
            end
        end
    end
    println("O valor aproximado da raiz é = ", m)
end
