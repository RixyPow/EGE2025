with open('24.4.txt') as f:
    s=f.readline()
    k=0
    mx=0
    for i in range(len(s)):
        if s[i]=='B':
            k+=1
            mx=max(mx, k)
        else:
            k=0
    print(mx)