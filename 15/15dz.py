p=list(range(17,23))
q=list(range(6,15))
a=list(range(1,48))
for x in range(1, 130):
    F=((not(x in a)) <= (x in p)) <= ((x in a) <= (x in q))
    if F==False:
        a.remove((x))
print(len(a),a)