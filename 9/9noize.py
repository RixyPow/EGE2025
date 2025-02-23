with open('9hdz.txt') as f:
    k=0
    for s in f:
        a=sorted(int(x) for x in s.split())
        povt=[y for y in a if a.count(y) == 4]
        nepovt = [y for y in a if a.count(y) ==1]
        if len(povt)==4 and ((sum(povt)/4) < (sum(a)/7)):
            k+=1
    print(k)
