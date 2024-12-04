with open('24_17616.txt') as f:
    s=[x for x in f]
    k=0
    mx=0
    for i in range(len(s)-1):
        if s[i]!='+' and s[i]!='*':
            k+=1
            mx=max(k, mx)
        if s[i]+s[i+1]=='0*':
            k=0
    print(mx)