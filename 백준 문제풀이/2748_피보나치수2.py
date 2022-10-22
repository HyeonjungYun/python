'''
N = int(input())
ans = [1,1]

for i in range(2,N):
    ans.append(ans[i-1] + ans[i-2])

print(ans[N-1])
'''
N = int(input())
a = b = 1
for i in range(N-2):
    a,b = b, a+b
print(b)