a = list(input())
for i in range(len(a)):
    if a[i].isupper() == True: a[i] = a[i].lower()
    elif a[i].islower() == True: a[i] = a[i].upper()
    print(a[i], end = "")