f = [int(x) for x in open("17var02.txt")]
a = [f[i] ** 2 + f[i - 1] ** 2 for i in range(1, len(f)) if f[i] + f[i - 1] == max(f)]
print(len(a), max(a))

# 4 9994000936
