'''
    自动获取存储属性名称
    为了避免在描述符声明语句中重复输入属性名,我们将为每个Quantity实例的斯特人哦热阿哥_name属性生成一个独一无二的字符串

'''
class Quanlity:
    __count=0;
    def __init__(self):
        cls=self.__class__;
        prefix=cls.__name__
        index=self.__count;
        self.strage_name='_{}#{}'.format(prefix,index)
        cls.__count+=1;
    def __get__(self,instance,owner):#owner参数是托管类的引用
        if instance is None:
            return self
        else:
            return getattr(instance,self.strage_name);
    
    def __set__(self,instance,value):
        if value>0:
            instance.__dict__[self.strage_name]=value;  #托管属性和类属性的名称不同,这里可以使用setattr和getattr
        else:
            raise 'value >0'

class LineItem:
    weight=Quanlity();
    height=Quanlity();

    def __init__(self,description,weight,price):
        self.description=description;
        self.weight=weight;
        self.price=price;
    def subtotal(self):
        return self.weight*self.weight;
print(LineItem.weight)