from sympy import symbols, Eq, solve

x = []
y = []
b = []
c = []
d = []
h = []
pnx = []
x_sym = symbols('x')


def read():
    print('Number of points:')
    n_points = int(input())
    for i in range(n_points):
        print(f'x{i}:')
        x.append(float(input()))
        print(f'y{i}:')
        y.append(float(input()))


read()
n = len(x)
intervals = n - 1
equations = []

for i in range(intervals):
    h.append(x[i + 1] - x[i])

for i in range(n):
    c.append(symbols(f'c{i}'))

for i in range(intervals):
    b.append(symbols(f'b{i}'))
    d.append(symbols(f'd{i}'))

c[0] = 0
c[intervals] = 0

a = y.copy()

print('initial a:', a, '| b:', b, '| c:', c, '| d:', d, '| h:', h)

for i in range(1, n - 1):
    equations.append(Eq(
        h[i - 1] * c[i - 1] + 2 * (h[i - 1] + h[i]) * c[i] + h[i] * c[i + 1],
        (3 / h[i]) * (a[i + 1] - a[i]) - (3 / h[i - 1]) * (a[i] - a[i - 1])
    ))

solution = solve(equations, c[1:intervals])
for i in range(1, intervals):
    c[i] = solution[c[i]]

for i in range(intervals):
    d[i] = (c[i + 1] - c[i]) / (3 * h[i])

print()
for i in range(intervals):
    b[i] = (1 / h[i]) * (a[i + 1] - a[i]) - (h[i] / 3) * (2 * c[i] + c[i + 1])

print('final a:', a, '| b:', b, '| c:', c, '| d:', d)

for i in range(intervals):
    if i == intervals - 1:
        print(f'[{x[i]},{x[intervals]}]:')
    else:
        print(f'[{x[i]},{x[i + 1]}]:')

    print(
        f'S{i}(x) = {a[i]} + ({b[i]})(x - {x[i]}) + '
        f'({c[i]})(x - {x[i]})^2 + ({d[i]})(x - {x[i]})^3'
    )

    pnx.append(
        a[i]
        + b[i] * (x_sym - x[i])
        + c[i] * (x_sym - x[i]) ** 2
        + d[i] * (x_sym - x[i]) ** 3
    )

point = float(input('Enter x to evaluate: '))
for i in range(intervals):
    if x[i] <= point <= x[i + 1]:
        print('result:', pnx[i].subs(x_sym, point))
        break
else:
    print('the point is outside the interpolation range.')