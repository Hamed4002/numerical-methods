x = []
f = []
delta = []


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

if d not in x:
    print('the point must be one of the nodes.')
    exit()

index = x.index(d)
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

p = 0
sign = -1
for i in range(len(delta)):
    sign = sign * (-1)
    p += (1 / h) * (delta[i] / (i + 1)) * sign

print(p)