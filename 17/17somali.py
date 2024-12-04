with (open('17.10.txt') as f):
    h=[]
    s=[int(x) for x in f]
    for i1 in range(len(s)):
        for i2 in range(i1, len(s)):
            if (s[i1]+s[i2])%120==0:
                h.append(s[i1]+s[i2])
    print(len(h), max(h))