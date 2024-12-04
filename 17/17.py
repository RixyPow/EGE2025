with open("17.8.txt") as f:
    s=[int(x) for x in f]
    k=[]
    for i in range(len(s)-1):
        if ((s[i]%5)==0 or (s[i+1]%5)==0) and str(s[i]).count('1')>=1 and str(s[i+1]).count('1')>=1:
            k.append(s[i]+s[i+1])
    print(len(k), max(k))



