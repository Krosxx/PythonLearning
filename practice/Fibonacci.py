
a=0
b=1

while b<100:
    print(b)
    temp=b
    b=a+b
    a=temp

#--->
a,b=0,1
while b<100:
    print(b,end=',')
    a,b=b,a+b
