def even(n):
    if int(n) % 2 == 0: return int(n)
    else: return 0
for i in range(int(input())):
    a = list(map(even, input().split()))
    a = [i for i in a if i not in {0}]
    print(sum(a), min(a))
