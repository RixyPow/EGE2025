with open('17.4.txt') as f:
    k=[]
    s=[int(x) for x in f]
    for i in range(len(s)-2):
        for j in range(i+1, len(s)):
            if (s[i]+s[j])%9==0:
                k.append(s[i]+s[j])
    print(len(k), max(k))