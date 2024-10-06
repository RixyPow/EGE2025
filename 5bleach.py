for n in range(100, 1000):
    s=str(n)
    kek1=int(str(int(s[0])*int(s[1])))
    kek2=int(str(int(s[1])*int(s[2])))
    if kek1>=kek2:
        kek3=str(kek1)+str(kek2)
    else:
        kek3=str(kek2)+str(kek3)
    if int(kek3)==123:
        print(n)
