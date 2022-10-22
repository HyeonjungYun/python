import sys
a = []
for i in range(int(input())):
    a, b = map(int,sys.stdin.readline().split())
    print("You get",a//b,"piece(s) and your dad gets", a%b,"piece(s).")