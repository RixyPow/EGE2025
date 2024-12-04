with open('24.6.txt') as f:
    s=f.readline()
    mx=0
    l=0

    a=0
    b=0
    for r in range(len(s)):
        a += s[r]=='A'
        b += s[r]=='B'
        while a>2 or b>2:
            a -= s[l]=='A'
            b -= s[l]=='B'
            l+=1
        mx=max(mx, r-l+1)
    print(mx)