# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。
a='aaaa'
b=99
print("a:{a} b:{b:5d}".format(a='sss',b=11))
print("a:{} b:{:5d}".format('sss',11))
print("a:{0} b:{1:5d}".format('sss',11))

print(repr(a).replace('a','b',1))
print(repr(a).center(11))
print(repr(b))

table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))