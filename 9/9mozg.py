with open('9_58322.txt') as f:
    k=0
    for s in f:
        a=sorted(int(x) for x in s.split())
        if ((a[3]**2) > (a[0] * a[1] * a[2])) or ((a[3]-a[2] == a[2]-a[1] == a[1]-a[0])):
            k+=1
    print(k)