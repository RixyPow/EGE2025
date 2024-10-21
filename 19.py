def F(a,s,m):
    if  a*s >= 144: return m%2==0
    if m==0: return 0
    h=[F(a+1, s, m-1), F(a*2, s, m-1), F(a, s+1, m-1), F(a, 2*s, m-1)]
    return any(h) if (m-1)%2==0 else all(h)
print([s for s in range(1,143) if not F(1, s, 2) and F(1, s, 4)])