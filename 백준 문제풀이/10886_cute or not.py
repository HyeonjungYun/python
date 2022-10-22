N = int(input())
count = 0
for i in range(N):
    if input() == '1': count += 1
if count > N - count: print("Junhee is cute!")
elif count < N - count : print("Junhee is not cute!")