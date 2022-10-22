for i in range(int(input())):
    N = str(bin(int(input()))[2:])[::-1]
    for j in range(len(N)):
        if N[j] == '1': print(j, end = " ")