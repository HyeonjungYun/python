def rev(n): return int(n[::-1])
a,b = input().split()
print(rev(str(rev(a) + rev(b))))