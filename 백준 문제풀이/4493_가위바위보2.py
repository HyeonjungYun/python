def vic (a,b):
    if (a == 'R' and b == 'S') or (a == 'P' and b == 'R') or (a == 'S' and b == 'P'):
        return 1
    elif (a == 'S' and b == 'R') or (a == 'R' and b == 'P') or (a == 'P' and b == 'S'):    
        return 0
    elif a == b:
        return 2


for i in range(int(input())):
    aw = 0; bw = 0
    for j in range(int(input())):
        a,b = input().split()
        c = vic(a,b)
        if c == 1: aw += 1
        elif c == 0: bw += 1
    if aw == bw: print('TIE')
    elif aw > bw: print("Player 1")
    elif aw < bw: print("Player 2")