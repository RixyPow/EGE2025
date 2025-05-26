with open('17.2may.txt') as f:
    s=[int(x) for x in f]
    a13=[x for x in s if abs(x)%100==13]
    m=max(a13)
    h=[]
    for i in range(len(s)-2):
        if ((s[i] in range(100, 1000)) +  (s[i+1] in range(100, 1000)) + (s[i+2] in range(100, 1000)))==2 and (s[i]+s[i+1]+s[i+2])<m:
            h.append(s[i]+s[i+1]+s[i+2])
    print(len(h), min(h))
