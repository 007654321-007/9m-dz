n = int(input())
m = 0
while(n > 0):
    a = n % 10
    m += a
    n = n//10
print(m)