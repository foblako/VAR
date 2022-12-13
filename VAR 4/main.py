for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = (w and (x <= y)) and (x or (y != z))
                print(x, y, w, z, f)
