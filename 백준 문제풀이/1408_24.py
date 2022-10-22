from datetime import*

t1 = datetime.strptime(input(), "%H:%M:%S")
t2 = datetime.strptime(input(), "%H:%M:%S")
t24 = datetime.strptime('00:00:00', "%H:%M:%S")
t10 = datetime.strptime('10:00:00', "%H:%M:%S")

if t1 > t2:
    print(str(t24 - t1 + t2)[-8:])
elif t1 < t2:
    if str(t2 - t1)[1] == ':':
        print("0", end = "");print(str(t2 - t1))
    else:
        print(t2 - t1)