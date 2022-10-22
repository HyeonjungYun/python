for i in range(int(input())):
    ans = [0,0]
    for j in range(int(input())):
        N = input().split()
        N[0] = int(N[0]); N[1] = float(N[1])
        ans[0] += N[0]
        ans[1] += N[0] * N[1]
    ans[1] = ans[1] / ans[0]
    print(ans[0], round(ans[1],1))