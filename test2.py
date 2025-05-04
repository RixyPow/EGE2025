with open('17.1may.txt') as f:
    s=[int(x) for x in f]
    chet=[y for y in s if y%2==0]
    h=sum(chet)/len(chet)
    for i in range(len(s)-1):
        if (s[i]%3==0 or s[i+1]%3==0) and (s[i]<)