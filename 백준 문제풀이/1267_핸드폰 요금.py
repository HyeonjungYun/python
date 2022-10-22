from math import*


input()
a = list(map(int, input().split()))
Y = []
M = []
for j in a:
    Y.append(ceil((j+1)/30)*10)
    M.append(ceil((j+1)/60)*15)
if sum(Y) > sum(M): print("M", sum(M))
elif sum(Y) < sum(M): print("Y", sum(Y))
else: print("Y","M",sum(Y))