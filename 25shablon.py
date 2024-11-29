from fnmatch import *
for x in range(1991, 10**8+1, 1991):
    if fnmatch(str(x), '3?1*57'):
        print(x, x//2024)
