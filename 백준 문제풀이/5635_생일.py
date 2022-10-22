import datetime

N =[]; date = []
for i in range(int(input())):
    N.append(list(input().split()))
    for j in range(1,4):
        N[i][j] = int(N[i][j])
    date.append(datetime.datetime(N[i][3], N[i][2], N[i][1]))
print(N[date.index(max(date))][0])
print(N[date.index(min(date))][0])
