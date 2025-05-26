for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = not(x <= y) or (x == z) or w
                if F == False:
                    print(x, y, w, z)
