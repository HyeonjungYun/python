def pac(n):
    if n <= 1:
        return 1
    return n*pac(n-1)
print(pac(int(input())))