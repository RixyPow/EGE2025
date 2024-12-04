def F(x):
    return (x&21074!=0) <= ((x&12369)<=(x&A!=0))
for A in range(0,10000000):
    if all(F(x) for x in range(0,10000000)):
        print(A)