'''
x = []
y = []

for i in range(0, 3):
    N = []
    N = (list(map(int, input().split(maxsplit = 2))))
    x.append(N[0])
    y.append(N[1])

maxx = max(x)
maxy = max(y)
minx = min(x)
miny = min(y)

square = []
square.append([maxx, maxy])
square.append([minx, maxy])
square.append([maxx, miny])
square.append([minx, miny])

ans = []
for i in range(0,4):
    cor = 0
    for j in range(0, 3):
        if square[i] == [x[j], y[j]]:
           cor += 1 
    if cor == 0:
        ans = square[i]

print(ans[0],ans[1])
'''
x = []
y = []

for i in range(0, 3):
    N = []
    N = (list(map(int, input().split(maxsplit = 2))))
    x.append(N[0])
    y.append(N[1])

def compare(x):
    if x[0] == x[1]:
        return x[2]
    elif x[0] == x[2]:
        return x[1]
    elif x[1] == x[2]:
        return x[0]

resx = compare(x)
resy = compare(y)

print(resx, resy)