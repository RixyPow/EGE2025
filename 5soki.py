for i in range(7, 1000):
    n=bin(i)[2:]
    if i%3==0:
        n=n+n[-3]+n[-2]+n[-1]
    else:
        n=n+bin(3*(int(n, 2)%3))[2:]
    if int(n, 2)<100:
        print(i)