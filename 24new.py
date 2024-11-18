with open('24var18-20.txt') as f:
    s=f.readline()
    mx=0
    k=1
    for i in range(len(s)-1):
        if s[i]<s[i+1]:
            k+=1
            mx=max(mx, k)
        else:
            k=1
    print(mx)
