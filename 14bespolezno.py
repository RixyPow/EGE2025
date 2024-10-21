for x in range(1, 2031):
    s=7**170+7**100-x
    b=''
    while s>0:
        b=str(s%7)+b
        s//=7
    if b.count('0')==71:
        print(x)