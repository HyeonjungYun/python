for i in[0]*int(input()):
    n=int(input());i=0
    while n:
        if n&1:print(i)
        n=n>>1;i+=1

'''
n&1로 n의 이진수에서 가장 아래 칸이 0인지 1인지 판별
이후 n = n >> 1로 이진수를 한 칸씩 오른쪽으로 땡겨서 십의 자리의 수를 일의 자리 수로 끌어내림
i는 자리수 표현
'''