N = int(input())
for i in range(1, N+1):
    print(("* "*i).center(((N*2)-1))[:N+i-1])