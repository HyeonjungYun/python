N = int(input())
for i in range(0,N):
    print(('*'*(N-i)).rjust(N," "), end = "")
    print('*'*(N-i-1))
