with open('24.8.txt') as f:
    s=f.readline().replace('STO', '*')
    k=0
    mx=0
    for i in range(len(s)):
        if s[i]=='*':
            k+=1
            mx=max(mx, k)
        else:
            k=0
    print(mx)