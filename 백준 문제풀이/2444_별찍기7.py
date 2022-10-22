N = int(input())
for i in range(1,N+1):
    print(('*'*(i)).rjust(N," "), end = "")
    print('*'*(i-1))
for i in range(1,N):
    print(('*'*(N-i)).rjust(N," "), end = "")
    print('*'*(N-i-1))