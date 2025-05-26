from re import *
with open('24re.txt') as f:
    s=f.readline()
    num=r'([1-6]+)'
    reg=rf'B{num}([-*]{num})+'
    a=max([x.group() for x in finditer(reg, s)], key=len)
    print(len(a), a)