from sympy import symbols, expand, simplify

x_vals = [1, 2, 4]
f_vals = [161, 162, 164]
x = symbols('x')


def differences(x_vals, f_vals):
    n = len(f_vals)
    table = [[0] * n for _ in range(n)]

    for i in range(n):
        table[i][0] = f_vals[i]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            table[i][j] = (table[i][j - 1] - table[i - 1][j - 1]) / (
                x_vals[i] - x_vals[i - j]
            )

    return [table[n - 1][k] for k in range(n)]


def newton_polynomial(x_vals, f_vals):
    coefficients = differences(x_vals, f_vals)
    n = len(coefficients)
    sigma = coefficients[0]
    product = 1

    for i in range(1, n):
        product *= (x - x_vals[n - i])
        sigma += coefficients[i] * product

    return simplify(expand(sigma))


pnx = newton_polynomial(x_vals, f_vals)
print('pn(x):', pnx)