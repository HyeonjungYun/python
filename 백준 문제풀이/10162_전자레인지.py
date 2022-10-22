N = int(input())

def a(N):
    if N % 10 != 0: return -1
    else: return 1

def b(N, x, y, z):
    if N >= 300:
        x = N // 300
        N -= 300 * (N // 300)
    if N >= 60:
        y = N // 60
        N -= 60 * (N //60)
    if N >= 10:
        z = N // 10
    return x,y,z
x = 0; y = 0; z = 0
if a(N) == -1:
    print(-1)
else:
    x, y, z = b(N, x, y, z)
    print(x, y, z)