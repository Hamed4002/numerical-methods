from sympy import symbols, diff, factorial, expand

x = []
f = []
delta = []
sigma = []
s = symbols('s')


def read():
    print('Enter the number of points (k):')
    k = int(input())
    for i in range(k):
        print(f'x{i}:')
        x.append(float(input()))
        print(f'y{i}:')
        f.append(float(input()))
    print('Enter the point at which to differentiate (d):')


read()
h = x[1] - x[0]
d = float(input())

if d not in x or d == x[0]:
    print('invalid point.')
    exit()

index = x.index(d) - 1
count = len(x) - 1 - index
values = f.copy()

for step in range(count):
    new_delta = []
    for i in range(index, len(values) - 1):
        new_delta.append(values[i + 1] - values[i])
    values = new_delta
    delta.append(values[0])
    index = 0

print('delta:', delta)

expression = 1
for i in range(len(delta)):
    expression *= (s - i)
    expression = expand(expression)
    temp = diff(expression, s)
    print('sigma:', temp)
    sigma.append(temp.subs(s, 1))

print('sigma values:', sigma)

p = 0
for i in range(len(delta)):
    p += (1 / h) * (delta[i] * (sigma[i] / factorial(i + 1)))

print(p)