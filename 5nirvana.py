for n in range(10000):
    b=bin(n)[2:]
    sc = 0
    sn = 0
    for i in range(len(b)):
        if i%2==1 and b[i]=='1':
            sc+=1
        elif i%2==0 and b[i]=='0':
            sn+=1
    if abs(sc-sn)==5:
        print(n)