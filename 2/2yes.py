for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x==y)<=(not z or w)) == (not((w<=x) or (y <= z)))
                if F==True:
                    print(x, y, z, w)