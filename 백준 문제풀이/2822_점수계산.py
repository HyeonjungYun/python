a = []; b = []
for i in range(8):
    a.append(int(input()))
print(sum(sorted(a)[3:]))
for i in range(3,8):
    b.append(a.index(sorted(a)[i]) + 1)
print(" ".join(str(n) for n in sorted(b)))
