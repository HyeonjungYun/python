import math

N = int(input())

for i in range(0, N):
    aN = list(map(int, input().split()))
    print(math.lcm(aN[0], aN[1]))
