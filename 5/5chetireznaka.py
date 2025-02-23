for n in range(10000, 100000):
    s=str(n)
    a1 = int(s[0])+int(s[2])+int(s[4])
    a2 = int(s[1]) + int(s[3])
    if a1>=a2:
        a=str(a2)+str(a1)
    else:
        a = str(a1) + str(a2)
    if a=='723':
        print(n)