N = list(input())
y = []
z = N.count('A')
i = 0
while len(N) > 0:
    l = N.pop()
    y.append(l)
    if len(y) > 3 and y[-1] == 'P' and y[-2] == 'P' and y[-3] == 'A' and y[-4] == 'P':
        y.pop()
        y.pop()
        y.pop()
if y == ['P']: print('PPAP') 
else: print('NP')       