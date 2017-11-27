# import one
# print(one.o)

print('ab' in 'qweabc')

a=[1,2,3,4]
b=['a','b','c','d','e']
# for a,b in zip(a,b):
#     print(a,b)

for index,b in enumerate(b,1):
    print(index,b)

with open('smtp/user.json') as js:
    print(js.read())
