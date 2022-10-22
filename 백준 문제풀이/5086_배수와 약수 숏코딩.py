a=1
while a:
    a,b=map(int,input().split())
    a>0 == print({0:"neither",b%a:"factor",1:"multiple"}[a%b<1])