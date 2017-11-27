g = lambda x, y: x + y


def add(x, y):
    def sub():
        nonlocal x
        x = 6
        # print(x)

    sub()
    return x + y


a = 1
b = 1.0
# print(a is b)
#
# print(a==b)
c = None
print(not c is not None)

print(g(1, 2))
ii = [1, 2, 3, 4, 'five']
del ii[0]
assert len(ii) > 1

print(ii)

print(ii[3])


def create():
    list = range(3)
    re = 1
    for i in list:
        yield i * i


print(create())

with open(r'../retest.py') as stream:  # 无论是否异常 最后都会关闭文件流 相当try finally
    for line in stream:
        print(line)
with open('write.txt', 'w') as write:
    write.write("Hello")


def reTwoParas(a: object, b: object) -> object:
    return a, b


a, b = reTwoParas(1, 2)
print(a,b)
