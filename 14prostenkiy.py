for x in range(9):
    for y in range(9):
        s=2*9**4 + y*9**3 + 6*9**2 + 6*9 + x + x*12**3 + 0*12**2 + y*12 + 1
        if s%170==0:
            print(s//170)