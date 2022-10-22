for i in range(int(input())):
    a,b = input().split(); a = int(a)
    b = b[:a-1] + b[a:]
    print(b)