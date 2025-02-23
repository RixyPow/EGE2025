with open('24var02.txt') as f:
    s=f.readline().replace('5', '1').replace('6', '1').replace('7', '1').replace('8', '1')
    s=s.replace('-', '+')
    s=s.replace('++', '+ +')
while '+00' in s:
    s=s.replace('+00', '+0 +0')
s=s.replace('+01', '+0 1')
mx=0
for i in s.split():
    mx=max(mx, len(i.strip('+')))
    if mx==166:
        print(i)
        break
print(mx)
