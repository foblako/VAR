# 3028

a = 4 * 25 ** 2022 - 2 * 5 ** 2000 + 125 ** 1011 - 3 * 5 ** 100 - 660


def con(x):
    s = ""
    while x != 0:
        s += str(x % 5)
        x //= 5
    return s[::-1]


a = con(a)
print(a.count("4"))
