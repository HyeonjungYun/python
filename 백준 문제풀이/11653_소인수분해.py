from math import*
N = int(input())
aN = []
sosu = 0

while 1:
    ox = False
    for i in range(2, floor(sqrt(N))+1):
        if N % i == 0:
            aN.append(i)
            N = N // i
            ox = True
            break
    if ox == False:
        aN.append(N)
        break

for i in range(len(aN)):
    if N > 1:
        print(aN[i])