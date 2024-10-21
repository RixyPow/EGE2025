with open('9_58322.txt') as f:
    k=0
    for s in f:
        a=sorted(int(x) for x in s.split())
        povt=[y for y in a if a.count(y)>1]
        nepovt=[y for y in a if a.count(y)==1]
        if len(povt)>1 and len(nepovt)>=1 and ((sum(nepovt)/len(nepovt)) > (sum(povt)/len(povt))):
            k+=1
    print(k)
