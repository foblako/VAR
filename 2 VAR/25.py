from fnmatch import *

for x in range(0, 10 ** 8, 123):
    if fnmatch(str(x), "32*823"):
        print(x, x // 123)

# 32090823 260901
# 32213823 261901
# 32336823 262901
# 32459823 263901
# 32582823 264901
# 32705823 265901
# 32828823 266901
# 32951823 267901
