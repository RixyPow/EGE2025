for ss in range(10,500):
    for x in range(ss):
        for y in range(ss):
            if (2*ss**3 + 4*ss**2 + x*ss + 9 + y*ss**3 + x*ss**2 + y*ss + 3) == (x*ss**3 + 4*ss*2 + y*ss):
                print(x*ss**2+y*ss+y)