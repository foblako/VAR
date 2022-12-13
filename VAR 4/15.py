def tr(n, m, k):
    return n + m > k and n + k > m and m + k > n


def f(x, a):
    return not ((tr(x, 12, 20)) == (max(x, 5) <= 28) and tr(x, a, 3))


for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)

# 6
