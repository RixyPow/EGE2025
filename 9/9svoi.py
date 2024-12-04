with open('9.8.txt') as f:
    k=0
    for s in f:
        a=sorted(int(x) for x in s.split())
        if (a[2]**2==a[1]**2+a[0]**2) and (a[0]*a[1]/2) in range(14,51):
            k+=1
    print(k)