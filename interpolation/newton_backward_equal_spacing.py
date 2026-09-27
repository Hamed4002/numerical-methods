from sympy import symbols, expand, simplify, factorial

x_vals = [1, 2, 3]
f_vals = [161, 162, 163]

x = symbols('x')


def differences(f_vals):
    n = len(f_vals)
    deltas = [f_vals]
    for i in range(1, n):
        temp_delta = []
        for j in range(len(deltas[-1]) - 1, 0, -1):
            temp_delta.insert(0, deltas[-1][j] - deltas[-1][j - 1])
        deltas.append(temp_delta)
    return deltas


def newton_polynomial(x_vals, f_vals):
    deltas = differences(f_vals)
    h = x_vals[1] - x_vals[0]
    n = len(x_vals)
    sigma = f_vals[-1]
    product = 1

    for k in range(1, n):
        product *= (x - x_vals[-k]) / h
        sigma += (deltas[k][-1] / factorial(k)) * product

    return simplify(expand(sigma))


deltas = differences(f_vals)

pnx = newton_polynomial(x_vals, f_vals)
print(pnx)
print(pnx.subs(x, 2.5))