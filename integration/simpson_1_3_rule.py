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
        print(f'y{i}:')
        f.append(float(input()))

    h = x[1] - x[0]
    for i in range(len(x) - 1):
        if abs((x[i + 1] - x[i]) - h) > 1e-12:
            raise ValueError('the points must be equally spaced.')
    return h


h = read()
intervals = len(x) - 1
N = int(intervals / 2)

sigma = 0
for i in range(N):
    sigma += f[2 * i] + 4 * f[2 * i + 1] + f[2 * i + 2]

result = sigma * (h / 3)
print('approximate integral using composite Simpson 1/3 rule:', result)