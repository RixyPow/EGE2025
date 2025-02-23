for x in range(2):
    for y in range(2):
        for w in range(2):
            for u in range(2):
                F = (x<=w)<=(u<=y)
                if not F:
                    print(x, y, w, u)