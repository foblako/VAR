# 25
for n in range(1, 10000):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += "0"
    if n % 2 != 0:
        b += "1"
    if b.count("1") % 3 == 0:
        b = "11" + b[2:]
    if b.count("1") % 3 != 0:
        b = "10" + b[2:]

    if int(b, 2) <= 37:
        print(n)
