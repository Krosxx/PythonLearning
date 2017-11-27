
x=list(range(5,9))
y=list(range(10))#range(）生成数列
z=(list)(range(1,19,2))#步长
print(str(x))
print(y)
print(z)



for letter in 'abcdefg':
    print(letter,end=",")
print('\n')
for letter in 'Runoob':     # 第一个实例
   if letter == 'o':        # 字母为 o 时跳过输出
      # continue              #执行下一循环
      break
   print ('当前字母 :', letter)

list=range(10)
for index, item in enumerate(list):
    print(index, item)