a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) < sum(b): print(sum(b))
elif sum(a) >= sum(b): print(sum(a))