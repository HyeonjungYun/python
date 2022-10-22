from math import*

a = 1
while a:
    N = int(input())
    if N == -1:
        break
    ans = [1]
    n = floor(sqrt(N)) + 1

    for i in range(2,n):
        if N % i == 0:
            ans.append(i)
            ans.append(N//i)
    ans = sorted(list(set(ans)))

    for i in range(1,len(ans)):
        ans[0] += ans[i]
    
    if ans[0] == N:
        print(N,"= 1 +", end = " ")
        for i in range(1,len(ans) - 1):
            print(ans[i],"+", end = " ")
        print(ans[len(ans)-1])
    else:
        print(N,"is NOT perfect.")