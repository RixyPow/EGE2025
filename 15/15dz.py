p=list(range(25,51))
q=list(range(32,48))
a=list(range(25,48))
for x in range(1, 130):
    F=((not(x in a)) <= (x in p)) <= ((x in a) <= (x in q))
    if F==False:
        a.remove((x))
print(len(a),a)