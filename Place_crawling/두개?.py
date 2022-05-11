def f(l):
    l.append(1)
    return l


a = [2]

b = f(a)
print(b, a)
