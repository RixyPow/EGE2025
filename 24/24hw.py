with open('../24hw3.txt') as f:
    s=f.readline()
    k=0
    l=0
    mx=0
    for r in range(len(s)):
        k+=s[r]=='T'
        while k>100:
            k-=s[l]=='T'
            l+=1
        mx=max(mx, r-l+1)
    print(mx)