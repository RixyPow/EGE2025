with open('17ya4.txt') as f:
    h=[]
    s=[int(x) for x in f]
    a2025=[y for y in s if y%2025==0]
    mina=min(a2025)
    for i in range(len(s)-2):
        if ((s[i]+s[i+1]+s[i+2]) in range(100000,1000000)) and (((s[i]%mina)==0)+((s[i+1]%mina)==0)+((s[i+2]%mina)==0))>=1:
            h.append(s[i]+s[i+1]+s[i+2])
    print(len(h), max(h))