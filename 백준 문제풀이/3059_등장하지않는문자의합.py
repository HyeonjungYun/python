a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for j in range(int(input())):
    c = input()
    b = [n for n in a if n not in c]
    for i in range(len(b)):
        b[i] = ord(b[i])
    print(sum(b))