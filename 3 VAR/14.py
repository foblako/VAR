def c9(x):
    s = ""
    while x > 0:
        s += str(x % 9)
        x //= 9
    return s[::-1]


print(c9(243 ** 540 - 6 * 9 ** 530 + 21 * 3 ** 511 - 3 * 3 ** 70 - 200).count("8"))
# 1071
