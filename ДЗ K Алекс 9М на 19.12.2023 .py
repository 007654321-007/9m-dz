def bubble_sort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

a=int(input())
c=0
d=1
l=list(range(0,a)) 
for i in range(a):
    l[i]=int(input())
bubble_sort(l)
b=abs(l[a-1])
while (b>0):
    b=b//2
    c=c+1
for i in range(c-1):
    d=d*2
for i in range(a):
    if l[i]>=d:
       print(l[i]) 