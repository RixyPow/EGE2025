with open('107_17.txt') as f:
    k=[]
    s = [int(x) for x in f]
    a21=[y for y in s if y%21==0]
    mn=min(a21)
    for i in range(len(s)-1):
        if s[i]%mn==0 or s[i+1]%mn==0:
            k.append(s[i]+s[i+1])
    print(len(k), max(k))