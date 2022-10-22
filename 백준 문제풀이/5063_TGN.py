N = int(input())

for i in range(N):
    num = list(map(int, input().split()))
    sum = num[1] - num [0] - num[2]

    if sum < 0: print("do not advertise")
    elif sum > 0: print("advertise")
    else: print("does not matter")