from fnmatch import *

a = []
for i in range(0, 10 ** 8, 149):
    a.append(i)
for x in range(11000, 10 ** 8):
    if fnmatch(str(x), "11*223"):
        if x in a:
            print(x, x // 149)

# 1166223 7827
# 11000223 73827
# 11149223 74827
# 11298223 75827
# 11447223 76827
# 11596223 77827
# 11745223 78827
# 11894223 79827
