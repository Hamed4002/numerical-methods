from sympy import symbols, Eq, solve

x_values = []


def read():
    n_points = int(input('Enter the number of points: '))
    for i in range(n_points):
        print(f'x{i}:')
        x_values.append(float(input()))
    return n_points


n_points = read()
a = x_values[0]
b = x_values[-1]

x = symbols('x')
variables = symbols(' '.join(f'w{i}' for i in range(n_points)))

print('variables:', variables, 'x:', x, ', a:', a, 'b:', b)

equations = []
for i in range(n_points):
    expression = x ** i
    left = sum(variables[j] * expression.subs(x, x_values[j]) for j in range(n_points))
    right = (b ** (i + 1) - a ** (i + 1)) / (i + 1)
    print(f'equation {i} left:', left, 'right:', right)
    equations.append(Eq(left, right))

solution = solve(equations, variables)
print('solution:', solution)