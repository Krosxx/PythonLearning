import random

x=random.random()
print('x:',x)
x=random.choice(range(5,9))
y=random.choice(range(10))#range(）生成数列
if x > y:
    print('x:',x)
elif x == y:
    print('x+y', x + y)
else:
    print('y:',y)


n=100
sum = 0
counter = 1
while counter <= n:
    sum,counter = sum + counter,counter+1

print("1 到 %d 之和为: %d" % (n,sum))
print("1到%d 的和为：%d"%(n,sum))
