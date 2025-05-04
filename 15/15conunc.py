def F(x):
    return (((x & A) != 0) <= ((x&14==0) <= (x&17 != 0)))
for A in range(0,10000):
    if all(F(x) for x in range(0,10000)):
        print(A)