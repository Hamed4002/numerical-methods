x = []
f = []


def read():
    print('Enter the number of points (k):')
    k = int(input())
    for i in range(k):
        print(f'x{i}:')
        x.append(float(input()))
        print(f'y{i}:')
        f.append(float(input()))


read()
h = x[1] - x[0]

sigma = 0
for i in range(len(x) - 1):
    sigma += f[i] + f[i + 1]

result = sigma * (h / 2)
print('approximate integral:', result)