
def toStr(n, base):
    s = '0123456789ABCDEF'
    if n < base:
        return s[n]
    else:
        return toStr(n // base, base) + s[n % base]


print(toStr(125, 16))