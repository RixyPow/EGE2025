for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = ((x<=y)<=z) or (not w)
                if not F:
                    print(x, y, w, z)