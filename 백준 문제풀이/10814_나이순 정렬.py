import sys

def l(x): return int(x[0])
N = int(input())
x = [0]*N
for i in range(N):
    a,b = sys.stdin.readline().split()
    x[i] = ([a,b])
z = sorted(x, key = l)
for i in range(len(z)):
    sys.stdout.write(z[i][0]+" ")
    sys.stdout.write(z[i][1]+'\n')