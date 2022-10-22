b = input()
a = list(b)
c = ['']
for i in b:
    if i == '+': c[-1]= int(c[-1]);c.append(i);c.append('')
    elif i == '-': c[-1]= int(c[-1]);c.append(i);c.append('')
    else: c[-1] += i
c[-1] = int(c[-1])

ans = [0]
for i in c:
    if i == '+': pass
    elif i == '-': ans.append(0)
    else: ans[-1] += i
for j in range(1,len(ans)):
    ans[0] -= ans[j]
print(ans[0])