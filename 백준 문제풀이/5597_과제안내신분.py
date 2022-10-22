a = [n for n in range(1,31)]
for i in range(28):
    a.remove(int(input()))
print(*a)