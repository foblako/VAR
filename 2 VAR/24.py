s = open("24var02.txt").readline()
s = s.split("A")

m = 999999
for i in range(len(s) - 35):
    sub = ""
    for j in range(34):
        sub = sub + s[i + j] + "D"
    sub = sub + "D"
    m = min(m, len(sub))
print(m)

# 40
