with open('24 2.txt') as f:
    s=f.readline()
    k=0
    h=[]
    for i in range(len(s)-1):
        if s[i]=='E':
            h.append(s[i+1])
    p=sorted(h)
    k=1
    mx=0
    bukva=''
    for j in range(len(p)-1):
        if p[j]==p[j+1]:
            k+=1
            if k>mx:
                bukva=p[j]
                mx=k
        else:
            k=1
    print(bukva, mx)

