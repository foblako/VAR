print("x y w z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = x and (y <= z) and ((not y) <= ((not z) == w))
                print(x, y, w, z, f)
