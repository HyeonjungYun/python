N = input()
for i in N:
    if ord(i) < 68: print(chr(ord(i)-3+26), end = "")
    else: print(chr(ord(i)-3),end = "")