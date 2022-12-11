import itertools

k = 0
for i in itertools.product("КНОРСЯ", repeat=6):
    k += 1
    if ''.join(i).count("К") <= 3 and ''.join(i).count("Я") == 2:
        print(k)
        break
