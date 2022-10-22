a = []
import sys
for i in range(int(sys.stdin.readline())):
    c = list(sys.stdin.readline().split())
    if c[0] == "push_front": 
        a.insert(0, int(c[1]))
    elif c[0] == "push_back": 
        a.append(int(c[1]))
    elif c[0] == "pop_front": 
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop(0))
    elif c[0] == "pop_back": 
        if len(a) == 0:
            print(-1)
        else:
            print(a.pop())
    elif c[0] == "size": 
        print(len(a))
    elif c[0] == "empty": 
        if len(a) == 0:
            print(1)
        else :
            print(0)
    elif c[0] == "front": 
        if len(a) == 0:
            print(-1)
        else :
            print(a[0])
    elif c[0] == "back": 
        if len(a) == 0:
            print(-1)
        else :
            print(a[len(a)-1])