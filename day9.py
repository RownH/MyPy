class Person(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name=name
per=Person('rh',12)
print(per.name)
per.name='hello'
print(per.name)
