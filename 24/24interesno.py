with open('24.today.txt') as f:
    s=f.readline()
    h=[]
    k=0
    for i in range(len(s)):
        if s[i]=='8' and len(h)==0:
            h.append(s[i])
        elif len(h)>=1 and int(s[i], 36)<=9:
            h.append(s[i])
            k+=1
            if k==10:
                print(h)
        if int(s[i], 36)>9:
            k=0
            h=[]




