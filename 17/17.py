with open("17hdz.txt") as f:
    s=[int(x) for x in f]
    k=[]
    for i in range(len(s)-2):
        :
            k.append(s[i]+s[i+1]+s[i+2])
    print(len(k), max(k))



