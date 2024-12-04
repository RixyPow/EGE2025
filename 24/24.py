with open('../24.txt') as f:
    s=f.readline()
    mx=0
    l=0

    u=0
    v=0
    w=0
    x=0
    y=0
    z=0

    for r in range(len(s)):
        u += s[r] == 'U'
        v += s[r] == 'V'
        w += s[r] == 'W'
        x += s[r] == 'X'
        y += s[r] == 'Y'
        z += s[r] == 'Z'
        while u>100 or v>100 or w>100 or x>100 or y>100 or z>100:
            u -= s[l] == 'U'
            v -= s[l] == 'V'
            w -= s[l] == 'W'
            x -= s[l] == 'X'
            y -= s[l] == 'Y'
            z -= s[l] == 'Z'
            l+=1
            mx = max(r - l + 1, mx)
    print(mx)