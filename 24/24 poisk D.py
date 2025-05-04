with open('24fev31231231.txt') as f:
    s=f.readline().replace('LDR', '*').replace('LD', '#')
    k=0
    mx=0
    for i in range(len(s)):
        if s[i]=='*':
            k+=3
            mx=max(mx, k)
        elif s[i]=='#':
            k+=2
            mx=max(mx, k)
            k=0
        elif s[i]=='L':
            k+=1
            mx=max(mx, k)
            k=0
        else:
            k=0
print(mx)
