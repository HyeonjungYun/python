s=sorted
t,n=zip(*s((int(input()),i)for i in range(1,9))[3:])
print(sum(t),*s(n))

'''
*[1,2,3,4,5] -> 1 2 3 4 5
a = zip(a, b) -> a = (a,b)
'''