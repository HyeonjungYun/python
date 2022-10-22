N = int(input())
for i in range(1, 2*N):
    if i < N+1: print(('*'*i).rjust(N, " "))
    else: print(('*'*(2*N-i)).rjust(N, " "))
    