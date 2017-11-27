
#Strin
str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串



#List
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表


#Tuple（元组）
'''元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开。 

元组中的元素类型也可以不相同： 
'''
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123,)

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

# Dictionary 字典
tinyDict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}


print(tinyDict)  # 输出完整的字典
print(tinyDict.keys())  # 输出所有键
print(tinyDict.values())  # 输出所有

for str in tinyDict.values():
    print(str,end=", ")

a='name'
if(a in tinyDict.values()):
    print("t[",a,"] is none")
else:
    print(tinyDict[a],"not none")

a=tinyDict.copy()
del tinyDict['name']
tinyDict.clear()
b={'a':a}
print(b)

del b['a']
# del b
b['a']=a
a['name']='name'
a['code']+=1
print(b)

print(type(a) )
print(type(a) is dict)
