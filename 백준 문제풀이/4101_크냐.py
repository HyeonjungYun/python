running = True

while 1:
    N = list(map(int, input().split(maxsplit = 2)))
    if N[0] == 0 and N[1] == 0:
        break
    elif N[0] > N[1]:
        print("Yes")
    elif N[0] <= N[1]:
        print("No")
    