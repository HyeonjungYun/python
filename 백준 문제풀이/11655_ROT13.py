a = input()
for i in range(len(a)):
    if 65 <= ord(a[i]) <= 90:
        if (ord(a[i])+13) > 90 :
            print(chr((ord(a[i]) + 13)-26), end = "")
        else:
            print(chr(ord(a[i]) + 13), end = "")
    elif 97 <= ord(a[i]) <= 122:
        if (ord(a[i])+13) > 122 :
            print(chr((ord(a[i]) + 13)-26), end = "")
        else:
            print(chr(ord(a[i]) + 13), end = "")
    else: print(a[i], end = "")