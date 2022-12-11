a = [int(i) for i in open("17var03.txt")]
s = [a[i] + a[i - 1] + a[i - 2] for i in range(2, len(a)) if
     (((a[i] % 10 == 0 and a[i - 1] % 10 != 0 and a[i - 2] % 10 != 0) or (
         (a[i] % 10 != 0 and a[i - 1] % 10 == 0 and a[i - 2] % 10 != 0)) or (
           (a[i] % 10 != 0 and a[i - 1] % 10 != 0 and a[i - 2] % 10 == 0))) and a[i] + a[i - 1] + a[i - 2] < max(a))]
print(len(s), max(s))

# 203 99820
