N = int(input())
for i in range(1, 2*N):
    if i < N+1: print(('*'*i))
    else: print(('*'*(2*N-i)))