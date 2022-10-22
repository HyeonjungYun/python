N = int(input())
str = input()
A = 0
for i in range(N):
    if str[i] == 'A':
        A += 1

if A < N-A: print('B')
elif A > N-A: print('A')
else: print('Tie')