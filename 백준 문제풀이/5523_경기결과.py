import sys
aw = 0; bw = 0
for i in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    if a > b: aw += 1
    elif a < b: bw += 1
print(aw, bw)