a = int(input())
if a == 1: print(int(input())**2)
else:
    b = sorted(map(int, input().split()))
    print(b[0]*b[len(b)-1])