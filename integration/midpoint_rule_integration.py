x = []
f = []


def read():
    print('Enter the number of points (k):')
    k = int(input())
    if k % 2 == 0:
        raise ValueError('the number of points must be odd.')
    for i in range(k):
        print(f'x{i}:')
        x.append(float(input()))
        print(f'f{i}:')
        f.append(float(input()))
    n = int((k - 1) / 2)
    return n


n = read()
h = (x[-1] - x[0]) / n
print('h:', h, 'n:', n)

total = 0
for i in range(n):
    midpoint = x[0] + (i + 0.5) * h
    closest_index = min(range(len(x)), key=lambda j: abs(x[j] - midpoint))
    print('closest_index:', closest_index)
    total += h * f[closest_index]

print(f'Integral from {x[0]} to {x[-1]}:', total)