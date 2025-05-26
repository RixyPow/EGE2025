from fnmatch import *
for x in range(31007, 10**10+1, 31007):
    if fnmatch(str(x), '1*34?5?9'):
        print(x, x//31007)
