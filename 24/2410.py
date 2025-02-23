with open('24var10.txt') as f:
    s=f.readline()
    h=[]
    mn=10**10
    for i in range(len(s)):
        if s[i]=='A':
            h.append(i)
    for j in range(len(h)-34):
        mn=min(mn, h[j+34]-h[j]+1)
print(mn)