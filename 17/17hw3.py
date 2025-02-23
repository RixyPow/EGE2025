with open('../17hw3.txt') as f:
    h=[]
    s=[int(x) for x in f]
    a19=[y for y in s if y%100==19]
    for i in range(len(s)-2):
        if (s[i]%3==0 or s[i+1]%3==0 or s[i+2]%3==0) and ((s[i] in range(1000, 10000)) + (s[i+1] in range(1000, 10000)) + (s[i+2] in range(1000, 10000))) == 2 and (s[i]+s[i+1]+s[i+2]>max(a19)):
            h.append(s[i]+s[i+1]+s[i+2])
    print(len(h), max(h))