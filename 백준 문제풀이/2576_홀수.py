a = []
for i in range(7):
    N = int(input())
    if N % 2 == 1:
        a.append(N)
if len(a) < 1:
    print(-1)
else:
    print(sum(a),min(a))
