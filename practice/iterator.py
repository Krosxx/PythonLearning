import sys

#迭代
list=(list)(range(1,10))

it=iter(list)

for i in it:
    print(i,end=",")

it=iter(list)#it
while 1:
    try:
        print(next(it))
    except:
        sys.exit(0)