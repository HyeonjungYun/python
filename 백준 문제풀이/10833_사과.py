ans = []
for i in range(int(input())):
    a,b = map(int, input().split())
    ans.append(b % a)
print(sum(ans))