with open('24var05.txt') as f:
    s=f.readline()
    h=[]
    mn=10**10
    for i in range(len(s)):
        if s[i] == 'A':
            h.append(int(i))
    for j in range(len(h)-2023):
        mn=min(mn, h[j+2023]-h[j]+1)
    print(mn)