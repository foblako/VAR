# 12


for i in range(1000):
    b = bin(i)[2:]
    if i % 2 == 0:
        b += "0"
    else:
        b += "1"

    if b.count("1") % 3 == 0:
        b = b[:-2] + "11"
    else:
        b = b[:-2] + "10"

    if int(b, 2) >= 26:
        print(i)
        break
