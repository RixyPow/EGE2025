def F(s, m):
    if s<= 17: return m%2==0
    if m==0: return 0
    h=[F(s-5, m-1)]
    if s%2==0: h.append(F(s/2, m-1))
    if s%3==0: h.append(F(s/3, m-1))
    if s%2!=0 and s%3!=0: h.append(F(s+1, m-1))
    return any(h) if (m-1)%2==0 else all(h)
print([s for s in range(18,100) if F(s, 2)]) #19
print([s for s in range(18,100) if not F(s, 1) and F(s, 3)]) #20
print([s for s in range(18,100) if not F(s, 2) and F(s, 4)]) #21