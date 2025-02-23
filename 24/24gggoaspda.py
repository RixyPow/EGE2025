with open('24ya4.txt') as f:
    s=f.readline().replace('L', 'K').replace('M', 'K').replace('N', 'K')
    s=s.replace('2', '1').replace('3', '1')
    mx=0
    for i in range(len(s)):
        k=0 #letters
        h=0 #numbers
        for j in range(i, len(s)):
            if s[j]=='K':
                k+=1
            else:
                h+=1
            if k==2*h:
                mx=max(mx, k+h)
    print(mx)
