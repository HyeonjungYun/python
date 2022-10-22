a = int(input())
while 1:
    N = int(input())
    if N == 0: break
    if N % a == 0:
        print(f"{N} is a multiple of {a}.")
    else:
        print(f"{N} is NOT a multiple of {a}.")