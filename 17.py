with open("17.txt") as f:
    s=[int(x) for x in f]
    s19=[y for y in s if y%100==19]
    k=[]
    for i in range(len(s)-2):
        if ((s[i] in range(1000,10000)) + (s[i+1] in range(1000,10000)) + (s[i+2] in range(1000,10000)))==2 and ((s[i]%3==0) + (s[i+1]%3==0) + (s[i+2]%3==0))>=1 and (s[i]+s[i+1]+s[i+2])>max(s19):
            k.append(s[i]+s[i+1])
    print(len(k), max(k))

