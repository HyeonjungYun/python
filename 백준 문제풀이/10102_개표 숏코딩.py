N=int(input())
S=input().count('A')*2
print(['AB'[N>S],"Tie"][N==S])

'''
list count함수를 이용하여 갯수를 셈
카운트한 A의 갯수를 곱하기2 후에 최초에 입력한 케이스의 숫자와 비교하여
A와 B 중 어느 것이 크고 작은지 판별
'''