a=input()+'0'
print('FDCBA'.find(a[0])+.3*'0+'.find(a[1]))

'''
1번에 뒤에 0을 붙이는 이유는 F때문에, F가 입력될 때에는 +,-,0가 입력되지 않기 때문에
+3*'0+' 뒤부터 오류 발생
'FDCBA'.find(a[0])에서 인덱스 값을 그대로 성적으로 활용하고
+.3*'0+'.find(a[1]) find함수에서 해당 인덱스를 못 찾는 경우에 -1을 출력하는 것을 활용해
-가 붙는 점수를 계산함

'''