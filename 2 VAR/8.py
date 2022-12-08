from itertools import *

k = 0
for i in product("0123", repeat=5):
    s = "".join(i)
    if s[0] != "0":
        if s.count("3") == 1:
            if s.count("30") == 0 and s.count("03") == 0:
                k += 1
print(k)

# 174
