N = int(input())
sum = 0
i = 0
while 1:
    if sum == N:
        break
    elif sum > N:
        i -= 1
        break
    i += 1
    sum += i

print(i)