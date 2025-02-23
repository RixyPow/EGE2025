with open('9_fev.txt') as f:
    k=0
    for s in f:
        a=sorted(int(x) for x in s.split())
        povt=[y for y in a if a.count(y)==3]
        nepovt=[y for y in a if a.count(y)==1]
        if len(povt)==3 and sum(povt)/3 >= sum(nepovt)/3:
            k+=1
    print(k)