def toym(n, nox=False):
    d='0123456789abcdefgh'
    if 17 > len(d):
        return None
    m=''
    while n > 0:
        m=d[n % 17] + m
        n//=17
    return m.nox() if nox else m

x=int(input())
print(toym(x))