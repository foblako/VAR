def tr(n, m, k):
    p = m + n + k / 2
    return n + m > k and n + k > m and m + k > n and (p * (p - n) * (p - m) * (p - k)) ** 0.5 > 0


def f(x, a):
    return not ((tr(x, 11, 18) == (not (max(x, 5) > 15))) and tr(x, a, 5))


for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 1000)):
        print(a)

# 24
