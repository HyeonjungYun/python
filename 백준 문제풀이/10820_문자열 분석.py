while True:
    try:
        N = input()
        q,w,e,r = 0,0,0,0
        for i in N:
            if i.islower() == True: q += 1
            elif i.isupper() == True: w += 1
            elif i.isdigit() == True: e += 1
        r += N.count(" ")
        print(q,w,e,r)
    except:
        break