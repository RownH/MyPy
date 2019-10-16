'''
    19.2 使用特性验证属性
    @property装饰只读特性
    19.2.1 LineItem类:表示订单商品中的类
'''
class LineItem:
    def __init__(self,description,weight,price):
        self.description=description
        self.weight=weight;
        self.price=price
    def subtotal(self):
        return self.weight *self.price  #当出现 负数时 无法理解
    
#把数据改为特性 能验证值的特性
class LineItem1:
    def __init__(self,description,weight,price):
        self.description=description
        self.weight=weight;
        self.price=price
    def subtotal(self):
        return self.weight *self.price  #当出现 负数时 无法理解
    @property
    def weight(self):
        return self.__weight
    
    # 被装饰的读值方式有个__setter属性,这个属性也是装饰器 这个装饰其将渎值方式和设值方式绑定在一起
    @weight.setter 
    def weight(self,value):
        if value>0:
            self.__weight=value;
        else:
            raise ValueError('value mustbe >0')
    
a=LineItem1('',2,2);
a.weight=-1;
