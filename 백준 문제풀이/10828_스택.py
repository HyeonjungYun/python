a = []
import sys
for i in range(int(sys.stdin.readline())):
    c = list(sys.stdin.readline().split())
    if c[0] == "push": 
        a.append(int(c[1]))
    elif c[0] == "pop": 
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop())
    elif c[0] == "top": 
        if len(a) == 0:
            print(-1)
        else :
            print(a[len(a)-1])
    elif c[0] == "size": 
        print(len(a))
    elif c[0] == "empty": 
        if len(a) == 0:
            print(1)
        else :
            print(0)