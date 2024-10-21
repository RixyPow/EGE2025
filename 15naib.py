for a in range(100):
    for x in range(100):
        for y in range(100):
            if not((x<4) or (x>=20) or (y >= 3*x + a) or (y<100)):
                