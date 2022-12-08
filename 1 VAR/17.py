# 2 9997800125

s = [int(i) for i in open("17/17var01.txt")]
a = [s[i + 1] ** 2 + s[i] ** 2 for i in range(len(s) - 1) if (s[i + 1] + s[i]) == max(s)]
print(len(a), max(a))
