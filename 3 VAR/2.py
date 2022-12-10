print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = not (not y or (not( not z or w))) and (z or ((not w) == x))
                print(x, y, w, z, f)
