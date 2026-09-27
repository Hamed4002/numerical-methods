from sympy import symbols, Eq, solve

x = [0, 1, 2, 3]
y = [1, 2, 0, 2]

a = y.copy()
b = []
c = []
d = []
h = x[1] - x[0]
n = len(x)
intervals = n - 1
equations = []

for i in range(n):
    b.append(symbols(f'b{i}'))
    c.append(symbols(f'c{i}'))
    d.append(symbols(f'd{i}'))

c[0] = 0
c[intervals] = 0

print('c =', c, 'b =', b, 'd =', d, 'a =', a)

for i in range(1, intervals):
    equations.append(Eq(
        h * c[i - 1] + 2 * (2 * h) * c[i] + h * c[i + 1],
        (3 / h) * (a[i + 1] - a[i]) - (3 / h) * (a[i] - a[i - 1])
    ))

solution = solve(equations, c[1:intervals])
for i in range(1, intervals):
    c[i] = solution[c[i]]

for i in range(intervals):
    d[i] = (c[i + 1] - c[i]) / (3 * h)

print('new c:', c, 'new d:', d)

for i in range(intervals):
    b[i] = (1 / h) * (a[i + 1] - a[i]) - (h / 3) * (2 * c[i] + c[i + 1])

print('new b:', b)

for i in range(intervals):
    print(
        f'S{i}(x) = {a[i]} + ({b[i]})(x - {x[i]}) + '
        f'({c[i]})(x - {x[i]})^2 + ({d[i]})(x - {x[i]})^3'
    )