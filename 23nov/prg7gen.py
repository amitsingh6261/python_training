def demo():
    yield 11
    yield 13
    yield 14

x=demo()
print(next(x))
print(next(x))
print(next(x))
print("--------------------")

# ya phir

for x in demo():
    print(x)