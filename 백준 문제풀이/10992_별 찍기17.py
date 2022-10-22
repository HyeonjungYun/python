N = int(input())
for i in range(N):
    if i == 0:
        print("*".rjust(N, " "))
    elif 0 < i < N-1:
        print((("*"+" "*(1+2*(i-1))+"*").center(2*N-1, " "))[:N+i])
    elif i == N-1:
        print("*"*(2*N-1))