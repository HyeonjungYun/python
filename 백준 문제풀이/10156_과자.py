N = list(map(int, input().split()))

cookie = N[0] * N[1]
money = 0

if cookie > N[2]:
    money = cookie - N[2]

print(money)