for n in range(100, 1000):
    s=str(n)
    a1 = int(s[0])+int(s[1])
    a2 = int(s[1]) + int(s[2])
    if a1>=a2:
        a=str(a1)+str(a2)
    else:
        a = str(a2) + str(a1)
    if a=='1412':
        print(n)