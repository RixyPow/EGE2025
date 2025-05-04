l=['A', 'B', 'C', 'D']
with open('24.txt') as f:
    s=f.readline()
    k=0
    mx=0
    for i in range(len(s)-1):
        if s[i] in l and s[i+1] in l:
            k=1
        else:
            k+=1
            mx=max(mx, k)
    print(mx)