N = int(input())
a = b = 1
for i in range(N-2):
    a,b = b, a+b
print(b)