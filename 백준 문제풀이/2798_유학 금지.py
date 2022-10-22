a = "CAMBRIDGE"
b = input()
b = [i for i in b if i not in a]
print(*b,sep='')