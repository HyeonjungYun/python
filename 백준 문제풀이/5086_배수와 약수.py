while 1:
    N = list(map(int, input().split()))

    if N[0] == 0 and N[1] == 0:
        break
    elif N[0] % N[1] == 0:
        print("multiple")

    elif N[1] % N[0] == 0:
        print("factor")

    elif N[0] % N[1] != 0 and N[1] % N[0] != 0:
        print("neither")