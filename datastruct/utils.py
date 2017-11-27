
#列表推导式
vec=[1,2,3]
list=['a ','b ','  c']
v1=[3*x for x in vec]
v2=[[item,item] for item in vec]
v3=[item.strip() for item in list]
v4=[2*item for item in vec if item<2]
print(v1)
print(v2)
print(list)
print(v3)
print(v4)

print([round(355/113,i) for i in range(1,10)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(matrix)
matrix+=vec
vec[1]='vec'
print(matrix)
print(vec)