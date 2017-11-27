import string
# open() 将会返回一个 file 对象，基本语法格式:open(filename, mode)

file=open("F:\Project\c/000.cpp",'w')
# print(file.read())
s= "#include<stdio.h>" \
    "int main()" \
    "{" \
    "  int a,b,sum;" \
    "  a=2600657;" \
    "  b=2600657;" \
    "  sum=a+b;" \
    "  printf(\"和为%d\n\",sum);" \
    "  return 0;" \
    "}" \

file.write(s)
file.close()

file=open('t.txt','w')
list=range(10)
for i in list:
    file.writelines(i.__str__()+'\n')
file.close()

file=open('t.txt','r')
s=file.readline()
for line in file:
    print(line,end='')
file.close()

f = open("foo.txt", "w")

num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )# 返回字符串数
print(num)
value = ('www.runoob.com', 14)
f.write(str(list))
f.write(str(value))
f.close()

with open("foo.txt", "r") as f:
    print(f.read())



''''''
'''
  r     以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 
  rb    以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。 
  r+    打开一个文件用于读写。文件指针将会放在文件的开头。 
  rb+   以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。 
  w     打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 
  wb    以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 
  w+    打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 
  wb+   以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。 
  a     打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 
  ab    以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 
  a+    打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 
  ab+   以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 
'''
'''f.seek()

如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。

from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：

seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符 

from_what 值为默认为0，即文件开头。下面给出一个完整的例子：
'''