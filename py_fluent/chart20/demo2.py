'''
    LineItem类第五版:一种新型描述符
    AutoStorage
        自动管理储存属性的描述符类
    Vlidated
        扩展AutoStorage类的抽象子类,覆盖__set__方法,调用必须由子类实现的validate方法

'''
import abc
class AutoStorage:
    __counter=0;

    def __init__(self):
        cls=self.__class__;
        prefix=cls.__name__;
        index=__counter;
        self.stage_name='_{}#{}'.format(prefix,index);
        cls.__counter+=1;
    
    def __get__(self,instance,owner):
        if instance is None:
            return self;
        else:
            return instance.getattr(instance,self.stage_name);

    def __set__(self,instance,value):
        instance.setattr(instance,value);

class Validated(abc.ABC,AutoStorage):
    def __set__(self,instance,value):
        super().__set__(instance,value)
    @abc.abstractmethod
    def validated(self,instance,value):
        '''return validated value or raise ValueError'''
class Quantity(Validated):
    def validated(self,instance,value):
        if value<=0:
            raise ValueError('value must >0')
        return value

class NonBlank(Validated):

    def validated(self,instance,value):
        value=value.strip();
        if len(value)==0:
            raise ValueError('value cannot be empty or blank')
        return value

