for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = (((z <= w) or (y==w)) and ((x or z)==y))
                if F:
                    print(x, y, w, z)