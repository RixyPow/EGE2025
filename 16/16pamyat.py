import sys
sys.setrecursionlimit(3000)
def F(n):
    if n == 0:
        return 0
    if n>0 and n%2==0:
        return n+F(n-1)
    if n%2==1:
        return 2*F(n-2)
print(F(26))