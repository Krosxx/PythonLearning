#生成器  yield 函数

#跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

#数据结构

# import practice.iterator
import practice.name___

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        yield b
        a, b = b, a + b

list=fibonacci(225)

for i in list:
    print(i)

print(dir(list))
print(__file__)
print(__package__)
print()