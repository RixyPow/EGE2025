with open('17.4.txt') as f:
    k=[]
    s=[int(x) for x in f]
    sr=[y for y in s if y%10==3]
    srch = sum(sr) / len(sr)
    for i in range(len(s)-1):
        for j in range(len(s) - 1):
            if ((max(s)%s[i]==0) or (max(s)%s[j]==0)) and (s[i]+s[j]>srch):
                k.append(s[i]+s[j])
    print(len(k), min(k))