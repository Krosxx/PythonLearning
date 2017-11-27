''''''''''+ 加 - 两个对象相加 a + b 输出结果 31 
- 减 - 得到负数或是一个数减去另一个数 a - b 输出结果 -11 
* 乘 - 两个数相乘或是返回一个被重复若干次的字符串 a * b 输出结果 210 
/ 除 - x 除以 y b / a 输出结果 2.1 
% 取模 - 返回除法的余数 b % a 输出结果 1 
** 幂 - 返回x的y次幂 a**b 为10的21次方 
// 取整除 - 返回商的整数部分 9//2 输出结果 4 , 9.0//2.0 输出结果 4.0 
'''

'''
abs(x) 返回数字的绝对值，如abs(-10) 返回 10 
ceil(x)  返回数字的上入整数，如math.ceil(4.1) 返回 5 

cmp(x, y)  如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用  使用 (x>y)-(x<y) 替换。  
exp(x)  返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045 
fabs(x) 返回数字的绝对值，如math.fabs(-10) 返回10.0 
floor(x)  返回数字的下舍整数，如math.floor(4.9)返回 4 
log(x)  如math.log(math.e)返回1.0,math.log(100,10)返回2.0 
log10(x)  返回以10为基数的x的对数，如math.log10(100)返回 2.0 
max(x1, x2,...)  返回给定参数的最大值，参数可以为序列。 
min(x1, x2,...)  返回给定参数的最小值，参数可以为序列。 
modf(x)  返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。 
pow(x, y) x**y 运算后的值。 
round(x [,n]) 返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。 
sqrt(x)  返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j 
'''
from math import ceil
import random
a = 21
b = 10

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("6 - c 的值为：", c)

a = 10
b = 5
c = a // b
print("7 - c 的值为：", c)
c=5
print(c is b)
c+=1

a = 10
b = 20

if (a and b):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if (a and b):
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

a = '1'
b = 20
list = [1, 2, 3, 4, 5]

if (a in list):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if (b not in list):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if (a in list):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")

print('11' and 12)

print(ceil(3.1))

list=[1,2,3,4]
print(random.choice(list))