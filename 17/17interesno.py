with open('../17.today.txt') as f:
    s=[int(x) for x in f]
    h=[]
    min5=[y for y in s if y%10==5]
    for i in range(len(s)-1):
        if (abs(s[i])%10)==(abs(s[i+1])%10) and ((abs(s[i])%9==0) + (abs(s[i+1])%9==0))==1 and ((s[i]**2+s[i+1]**2)<=((min(min5))**2)):
            h.append(s[i]**2+s[i+1]**2)
    print(len(h), max(h))