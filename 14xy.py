for p in range(10,60):
    for x in range(p+1):
        for y in range(p+1):
            a=2*p**3 + 4*p**2 + x*p + 9
            b=y*p**3 + x*p**2 + y*p + 3
            c=x*p**3 + 4*p**2 + y*p
            if a+b==c:
                print(x*p**2+y*p+y)