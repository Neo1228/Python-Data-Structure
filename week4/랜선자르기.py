def count(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    X = [0] * (n + 1)
    X[1] = 1
    X[2] = 2

    for i in range(3, n + 1):
        X[i] = X[i - 1] + X[i - 2]

    return X[n]


n = int(input())
print(count(n))
