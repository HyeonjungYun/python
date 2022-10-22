for i in range(3):
    j = 1
    a = input()
    ans = []; e = 1
    while j < 8:
        if a[j] == a[j-1]:
            e += 1
            if j == 7:
                ans.append(e)
        elif a[j] != a[j-1]:
            ans.append(e); e = 1
        j += 1
    print(max(ans))