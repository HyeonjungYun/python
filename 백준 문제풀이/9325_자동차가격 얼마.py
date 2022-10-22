for i in range(int(input())):
    pr = int(input())
    for j in range(int(input())):
        a, b = map(int,input().split())
        pr += a*b
    print(pr)
