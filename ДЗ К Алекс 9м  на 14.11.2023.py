n = int(input())
r=0
for n in range(0,n):
    m=input()
    for k in range(0,4):
        if ((int(m[k])%2)==(int(m[k+1])%2)):
            break
    else:
        r+=1
print(r)