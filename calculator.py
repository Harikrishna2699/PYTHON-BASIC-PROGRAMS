def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b


def si(p, r, t):
    return (p * r * t) / 100


def ci(p, r, t):
    return p * pow((1 + r / 100), t)


def sqr(num):
    return num ** 2


def sqrt(num):
    return num ** 0.5

print(add(10,15))
print(sub(10,15))
print(mul(10,15))
print(div(10,15))
print(si(10,15,50))








