for A in range(1,100000):
    for x in range(1, 100000):
        if not((x&21074 != 0) <= (((x&12369)==0) <= (x&A != 0))):
            break
    else:
        print(A)