# 502

s = open("24/24var01.txt").readline()

sub = s[0]
m = 0
for i in range(len(s)):
    if sub.count("A") <= 3:
        sub += s[i]
        m = max(m, len(sub))

    else:
        sub = s[i]
print(m)
