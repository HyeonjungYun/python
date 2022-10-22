x = y = 0
for i in range(0,3):
    a, b = map(int, input().split())
    x ^= a
    y ^= b
print(x, y)

'''
xor 연산을 통해 세가지의 숫자 중 두 번 나오지 않은 숫자를 찾기
사각형의 네점의 경우 
(30, 10)
(30, 30)
(10, 30)
(10, 10)
x절편만 모아보면 (30, 30, 10, 10)
y절편만 모아보면 (10, 30, 10, 30)
이렇게 같은 숫자 2개가 각 2개씩 나오는 패턴이 만들어진다.

그래서 3개의 점만이 주어졌을 때 
xor연산을 이용하여 두 번 반복되지 않은 하나의 숫자를 찾으면 쉽게 한 개의 점을 찾아낼 수 있다.
x절편만 보았을 때
x절편의 집합이 (10, 10, 30)이라고 할 때
10 ^ 10 = 0
0 ^ 30 = 30 이 된다.
x절편의 집합에 속한 세 원소를 순차적으로 xor연산을 하게 되면
같은 숫자가 없는 하나의 숫자를 찾는 것이 가능하다.
(30, 10, 30)이라고 했을 때
30 ^ 10 = 20
20 ^ 30 = 10
--> (30 ^ 10) ^ 30 = 10
'''