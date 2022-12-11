for n in range(1, 1000):
    b = bin(n)[2:]
    if (b.count("0") + b.count("1")) % 2 == 0:
        b = b[:len(b) // 2] + "1" + b[len(b) // 2:]
    if int(b, 2) >= 26:
        print(n)
        breakpoint()

# 12
