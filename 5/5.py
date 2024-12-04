for i in range(10000,100000):
    t1 = int(str(i)[0]) + int(str(i)[2]) + int(str(i)[4])
    t2 = int(str(i)[1]) + int(str(i)[3])
    if t1 > t2:
        t3 = str(t2) + str(t1)
    else:
        t3 = str(t1) + str(t2)
    if t3 == '723':
        print(i)