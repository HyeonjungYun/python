import sys
N = int(input())
h = [0]*N
for i in range(N):
    h[i] = (list(sys.stdin.readline().split()))
h.sort(key = lambda x: x[0])
h.sort(reverse = True, key = lambda x: int(x[3]))
h.sort(key = lambda x: int(x[2]))
h.sort(reverse = True, key = lambda x: int(x[1]))
for i in range(N): sys.stdout.write(h[i][0]+ "\n")