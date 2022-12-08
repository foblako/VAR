def f(x, a):
    return (x % 20 == 0) <= (not (x % 11 == 0)) or (x + a >= 300)


for a in range(1, 10000):
    if all(f(x, a) for x in range(1, 10000)):
        print(a)
        break

# 80
