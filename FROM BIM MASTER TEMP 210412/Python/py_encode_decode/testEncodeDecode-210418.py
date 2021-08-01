a = "\u0432"
b = u"\u0432"
c = b"\u0432"
d = c.decode('utf8')

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)

e = c.decode('unicode_escape')
print(type(e), e)