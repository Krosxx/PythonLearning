# lambda 匿名函数
# lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数
fun1 = lambda a, b: a+b

fun1(1, 2)


#变量作用域
'''Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的'''
'''
L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
'''
'''
global 和 nonlocal关键字 '''

num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    outer=6
    def fun2():
        nonlocal outer
        print(outer)
    fun2()
fun1()
print(num)


a = 10
def test():
    global a
    a = a + 1
    print(a)


test()