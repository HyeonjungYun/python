from math import*
N = int(input())

for i in range(0,N):
    a = input()
    a1 = a.split(maxsplit = 2)
    a1[0], a1[1] = int(a1[0]), int(a1[1])
    amin = min(a1[0], a1[1])
    ans = []
    rans = 1

    while 1:
        ox = False
        for i in range(2, floor(sqrt(amin))+1):
            if amin % i == 0:
                ans.append(i)
                amin = amin // i
                ox = True
                break
        if ox == False:
            ans.append(amin)
            break

    for k in range(0, len(ans)):
        if a1[0] % ans[k] == 0:
            a1[0] = (a1[0] // ans[k])
        if a1[1] % ans[k] == 0:
            a1[1] = (a1[1] // ans[k])
    ans.append(a1[0])
    ans.append(a1[1])

    for l in range(0, len(ans)):
        rans *= ans[l]

    print(rans)
    