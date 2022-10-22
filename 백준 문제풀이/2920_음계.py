a = [n for n in range(1,9)]
N = list(map(int, input().split()))
if N == a: print("ascending")
elif N == a[::-1]: print("descending")
elif sorted(N) == a: print("mixed")