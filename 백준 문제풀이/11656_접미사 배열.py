N = input()
n = []
for i in range(len(N)):
    n.append(N)
    N = N[1:]
print(*sorted(n))