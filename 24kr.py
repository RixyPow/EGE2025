with open('24.txt') as f:
    s=f.readline()
    h=[]
    mx=0
    cnt=1
    for i in range(len(s)-1):
        if s[i]=='E':
            h.append(s[i+1])
    h=sorted(h)
    for j in range(len(h)):
        if h[j]==h[j+1]:
            cnt+=1
        else:
            

