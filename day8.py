class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def study(self,course_name):
        print('%s is studing %s' % (self.name,course_name))
        
class Test:
    def __init__(self,foo):
        self.__foo=foo
    def __bar(self):
        print(self.__foo)
        print('__bar')
test=Test('rown')
test._Test__bar()