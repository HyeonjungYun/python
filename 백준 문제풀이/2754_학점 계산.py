N = input()
if N != 'F':
    *_,a,b = sorted(N)

grade = ['A', 'B', 'C', 'D']
ara = [4.0, 3.0, 2.0, 1.0]
if N == 'F':
    print(0.0)
else:
    c = ara[grade.index(b)]

    if a == '+':
        c += 0.3
    if a == '-':
        c -= 0.3


    print(c)