with open('24dzi.txt') as f:
    s=f.readline()
    k=0
    for i in range(len(s)-1):
        if s[i]+s[i+1]=='DE':
            k+=1
print(k)
