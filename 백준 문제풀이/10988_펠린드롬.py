N = input()

from math import*

a = ceil(len(N)/2)
for i in range(a):
    if N[i] != N[len(N)-i-1]:
        N = 1
        break

if N == 1: print(0)
else: print(1)
