N = str(int(input())*int(input())*int(input()))
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(N)):
    a[int(N[i])] += 1
for i in range(10):
    print(a[i])