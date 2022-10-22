import sys

def binary_search(a, x):
    start = 0
    end = len(a) - 1
    res = -1
    while start <= end:             
        mid = (start + end) // 2
        if x > a[mid]:            
            res = mid
            start = mid + 1
        else:                       
            end = mid - 1
    return res

for i in range(int(input())):
    l, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    d = 0
    b.sort()
    for j in a:
        d += binary_search(b, j) + 1
    print(d)