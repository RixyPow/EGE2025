A=1
while True:
    for x in range(1000):
        if (x&9 == 0) <= ((x&19 != 0) <= (x&A != 0)):
            break
        else:
            print(A)
        A+=1