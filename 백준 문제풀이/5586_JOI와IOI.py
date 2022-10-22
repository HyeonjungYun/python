a = input(); c = 0
print(a.count("JOI"))
for i in range(a[:-2].count('I')):
    b = a.find('I')
    if b > -1:
        if a[b+1] == 'O' and a[b+2] == 'I':
            c += 1
        a = a[:b] + a[b+1:]
print(c)