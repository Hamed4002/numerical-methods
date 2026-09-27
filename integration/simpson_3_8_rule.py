x = []
f = []


def read():
    print('Enter the number of points (k):')
    k = int(input())
    if (k - 1) % 3 != 0:
        raise ValueError('the number of points must satisfy (k - 1) % 3 == 0.')

    for i in range(k):
        print(f'x{i}:')
        x.append(float(input()))
        print(f'f{i}:')
        f.append(float(input()))

    h = (x[k - 1] - x[0]) / (k - 1)
    n = int((len(x) - 1) / 3)
    return h, n


h, n = read()
print('h:', h, 'n:', n)

integral = 0
for i in range(n):
    integral += (3 / 8) * h * (
        f[3 * i] + 3 * f[3 * i + 1] + 3 * f[3 * i + 2] + f[3 * i + 3]
    )

print(f'Integral from {x[0]} to {x[-1]}:', integral)