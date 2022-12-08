# 231

from itertools import *

ch = ["1", "3", "5", "7", ]
a = 0
for i in product("01234567", repeat=5):
    if i[0] != "0":
        if i.count("4") == 2:
            s4 = "".join(i).find("4")
            e4 = "".join(i).rfind("4")
            try:
                if "".join(i)[s4 - 1] not in ch and "".join(i)[s4 + 1] not in ch and "".join(i)[e4 - 1] not in ch and \
                        "".join(i)[e4 + 1] not in ch:
                    a += 1
            except:
                ...
print(a)
