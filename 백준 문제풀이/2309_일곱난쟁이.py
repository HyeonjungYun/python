N = []
for i in range(9):
    N.append(int(input()))
N = sorted(N)
for i in range(9):
    for j in range(i+1,9):
        if sum(N) - (N[i] + N[j]) == 100:
            N.remove(N[i])
            N.remove(N[j-1])
            break
    if len(N) < 9: break
for i in range(7):
    print(N[i])