s='>'+10*'1'+20*'2'+30*'3'
summa=0
while '>1' in s or '>2' in s or '>3' in s:
    s=s.replace('>1', '22>', 1)
    s=s.replace('>2', '2>', 1)
    s=s.replace('>3', '1>', 1)
    summa=sum([int(x) for x in s if x != '>'])
print(summa)