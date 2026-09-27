from sympy import symbols, expand, simplify

x_sym = symbols('x')
x = [2, 3, -4, 5]
f = [3, 4, -1, 6]


def L(i):
    result = f[i]
    for j in range(len(x)):
        if i != j:
            result *= (x_sym - x[j]) / (x[i] - x[j])
    return simplify(expand(result))


def p_n():
    p = 0
    for i in range(len(x)):
        p += L(i)
    return simplify(expand(p))


print(p_n())