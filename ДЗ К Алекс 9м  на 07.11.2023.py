a = int(input())
b = int(input())
if (a<b):
    for n in range(a,b):
        if (n//4*4==n):
            print(n)
else:
    for n in range(a,b,-1):
        if (n//4*4==n):
            print(n)    