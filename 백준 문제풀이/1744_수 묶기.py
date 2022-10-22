from sys import*

x = []
N = int(input())
for i in range(N):
    x.append(int(stdin.readline()))
x.sort(reverse = True)
ans = []
i = 0
while 1:
    if i >= N: break
    elif i == N-1: ans.append(x[i]);break
    elif x[i] > 1:
        if x[i+1] > 1:
            ans.append(x[i]*x[i+1])
            i += 2
        elif x[i+1] <= 1:
            for j in range(i,N):
                ans.append(x[j])
            break
    elif x[i] <= 1:
            for j in range(i,N):
                ans.append(x[j])
            break
ans.sort()
if ans[0] < 0:
    x = ans
    ans = []
    N = len(x)
    i = 0
    while 1:
        if i >= N: break
        elif i == N-1: ans.append(x[i]);break
        elif x[i] < 0:
            if x[i+1] < 0:
                ans.append(x[i]*x[i+1])
                i += 2
            elif x[i+1] >= 0:
                for j in range(i,N):
                    ans.append(x[j])
                break
        elif x[i] >= 0:
                for j in range(i,N):
                    ans.append(x[j])
                break
    ans.sort()
if ans.count(0) > 0:
    for i in range(ans.count(0)):
        ans.pop(0)
print(sum(ans))