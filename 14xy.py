for ss in range(5,100):
    for x in range(ss):
        for y in range(ss):
            if (3*ss+2)*(ss+4)== x*ss**2 + y*ss + 2:
                print(y*ss+x)