with open("17fev456456.txt") as f:
    s=[int(x) for x in f]
    a6=[y for y in s if abs(y)%10==6]
    k=[]
    for i in range(len(s)-1):
        if  ((s[i] in a6) + (s[i+1] in a6))==1 and (s[i]**2+s[i+1]**2)<(min(a6)**2):
            k.append(s[i]**2+s[i+1]**2)
    print(len(k), max(k))



