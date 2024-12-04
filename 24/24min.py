with open('24var01.txt') as f:
    s=f.readline()
    cnt=0
    k=[]
    mn=10**10
    for i in range(len(s)):
        if s[i]=='A':
            k.append(i)
    for j in range(len(k)-2023):
        cnt=k[j+2023]-k[j]+1
        mn=min(mn, cnt)
    print(mn, k)