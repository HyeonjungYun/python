e = 1
while e:
    a,b,c = input().split()
    if b == 'E': break
    if eval(a+b+c) == False:
        print(f"Case {e}: false")
    elif eval(a+b+c) == True:
        print(f"Case {e}: true")
    e += 1