for i in range(int(input())):
    a,b = map(int,input().split())
    con = 0
    for i in range(a,b+1):
        con += str(i).count('0')
    print(con)