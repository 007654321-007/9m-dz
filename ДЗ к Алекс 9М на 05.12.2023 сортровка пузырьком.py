def bubble_sort(l):
    n = len(l)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

a=int(input())
l=list(range(0,a)) 
for i in range(a):
    l[i]=int(input())
bubble_sort(l)
for i in range(a):
    print(l[i])
