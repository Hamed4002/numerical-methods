from sympy import symbols, expand, simplify, diff

x_sym = symbols('x')
x = [0, 1, 3]
f = [0, -2, 6]


def py(count):
    result = 1
    for k in range(count):
        result *= (x_sym - x[k])
    return simplify(expand(result))


def my_diff(count):
    return diff(py(count), x_sym)


print('p_n(x) =', py(3))
print("p_n'(x) =", my_diff(3))


def sigma(j):
    total = 0
    for i in range(j):
        total += f[i] / my_diff(j).subs(x_sym, x[i])
    return total


def pnx():
    expression = simplify(expand(
        f[0]
        + sigma(2) * (x_sym - x[0])
        + sigma(3) * (x_sym - x[0]) * (x_sym - x[1])
    ))
    return expression


print('pnx =', pnx())