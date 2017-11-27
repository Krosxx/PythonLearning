from classobject.People import People


class Student(People):
    __id='001'
    def __init__(self,id='001',name='星星',age=0,weight=10) :
        People.__init__(self,name,age,weight)
        self.__id=id

    def fun(self):
        return 'hello'

    def getId(self):
        return self.__id



stu=Student('00002','name')
print(stu.getId())
print(stu.name)
print(stu.fun())