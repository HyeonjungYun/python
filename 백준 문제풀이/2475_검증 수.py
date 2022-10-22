N = list(map(int,input().split())); N[0] = (N[0])**2
for i in range(1,5):
    N[0] += (N[i])**2
print(N[0]%10)