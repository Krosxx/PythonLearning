
import sys
from sys import path

print("Hello World")

total_num = 11 + \
            22 + \
            33 + 44

total_list = ['1', '\'2',
              3, 4, 1 + 2j,
              5.5, 6e4]
print(total_list)

a1 = 1 + 3j
a2 = 1 - 4j
print(a1 + a2)
print(a1 * a2)
print(a1 / a2)

str = r'1111 \n'  # 输出\n
print(str)

str = u"this is an unicode string"  # 处理unicode字符

print(str)
# str=input("input something")
print(str + str);
print(str + str, end="---->")

a1 = a2 = 1

if a1 > a2:
    print("a1>a2")
elif a1 == a2:
    print("a1==a2")
else:
    print("a1<a2")

print(path[len(path) - 1])

for i in sys.argv:
    print(i)

int_list = [11.2, 2, 3, 4, 66.1, 7, 8]
print(max(int_list))
# print(max(input("输入几个数")))

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

str1 = '123'
str2 = '45666666666'
print(3 * str1 + str2)
print(3 * 'str1' + str2[1] + str2[-1])
print(str2[2:5])
print(str2[-2:])

str2='qqqqqqq'+str2[1:]
print(str2.upper())
print(str2.__contains__('q1'))
a=123/2
print(a.__mod__(2))


'''+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1'''
