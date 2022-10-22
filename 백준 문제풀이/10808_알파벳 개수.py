a = [i for i in [0]*26]
b = list(input())
for i in range(len(b)):
    a[ord(b[i])-97] += 1
print(*a)