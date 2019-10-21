'''
    20.1 描述符实例:验证属性
    特性工厂借助函数试变成模式避免重复编写读取方法和设置方法

    描述符类
        实现描述符协议的类  比如Quantity类

    托管类:
        把描述符类是列声明为类属性的类 例如Lineitem

    描述符实例:
        描述符的各个实例,声明为托管类的类属性

    托管实例:
        托管类的实例
    
    储存属性:
        托管实例中存储自身托管属性的属性 
    
    托管属性:
        托管类中由描述符实例处理的公开属性,值存储在村数属性中,也就是说 描述符实例和存储属性为托管属性建立了基础

    Quanlity实例是LineItem的类属性


'''
#使用描述符管理LineItem的属性
class Quantity: #描述符协议实现 描述符类
    def __init__(self,storage_name):
        self.storage_name=storage_name;#托管实例存储值的属性名称

    def __set__(self,instance,value):   #instance 代表托管实例  这里指代LineItem
        if value>0:
            instance.__dict__[self.storage_name]=value;#将值存在托管实例中
        else:
            raise ValueError('value must be >0')
        #托管属性与存储属性名称相同,所以不需要定义__get__方法

class LineItem:
    weight=Quantity('weight');#类属性
    height=Quantity('height');

    def __init__(self,description,weight,price):
        self.description=description;
        self.weight=weight;
        self.price=price;   #存储属性

    def subtotal(self):
        return self.weight*self.height;

#异常无法获取


