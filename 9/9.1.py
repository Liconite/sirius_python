def nonNone(a, b, c):
    if a != None and b != None and c != None:
        return a, b, c
    else:
        return 0


def toNone(x):
    if x == "None":
        return None
    else:
        return x


a, b, c = input(), input(), input()
a, b, c = toNone(a), toNone(b), toNone(c)
print(nonNone(a, b, c))
