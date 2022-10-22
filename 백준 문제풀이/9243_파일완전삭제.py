a = int(input())
N = int(input(),2)
N1 = int(input(),2)
b = int('1'*(N.bit_length()),2)
for i in range(a):
    N ^= b
if N == N1: print("Deletion succeeded")
else: print("Deletion failed")