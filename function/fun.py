# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

def calArea(width, height):
    width = 2
    return width * height


a = 1
print(calArea(a, 2))
print(a)

'''必需参数'''
def changeString(str):
    str = 'str'

str = '1'
changeString(str)
print(str)


def changeList(li: list):
    li.append('3')
    li.append(li.copy())


list = ['1', 2]
l=list[:]
print('l:',l)
changeList(list)
print(list)
'''
参数

以下是调用函数时可使用的正式参数类型：

关键字参数:'''


def ab(a, b):
    print("a = %d,b = %d" % (a, b))


ab(b=2, a=1)

'''
默认参数
'''


def defaultPara(a, b=1):
    print(a, b)


defaultPara(2)

'''
不定长参数
加了星号（*）的变量名会存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组
'''


def uncertaintyLength(a, *tuple):
    print(tuple)
uncertaintyLength('1',2)
