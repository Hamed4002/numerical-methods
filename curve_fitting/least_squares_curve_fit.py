from sympy import symbols, diff, solve

x = []
f = []
diff_E_x = {}
ak = {}

print('Enter the number of points:')
n = int(input())


def adding():
    for i in range(n):
        print(f'x[{i}]:')
        x.append(float(input()))
        print(f'f[{i}]:')
        f.append(float(input()))


adding()

print('Enter the degree k:')
k = int(input())

for i in range(k + 1):
    ak[i] = symbols(f'a{i}')

E = 0
for i in range(len(x)):
    T = sum(ak[j] * (x[i] ** j) for j in range(k + 1))
    E += (T - f[i]) ** 2

for j in range(k + 1):
    diff_E_x[j] = diff(E, ak[j])

equations = [diff_E_x[j] for j in range(k + 1)]
solution = solve(equations, [ak[j] for j in range(k + 1)])

print('solution:', solution)