'''
    定义一个特性工厂
    我们将定义一个quanlity的特性函数,
    在这个应用中 要管理属性表示不能为负数或零的量

'''
   
def quantity(storage_name):
        def qty_gettter(isinstance):    #instance指代要把属性存储其中Lineitem
            return isinstance.__dict__[storage_name]    #instance_dict__获取 跳过特性 防止递归
        
        def qty_setter(isinstance,value):
            if value>0:
                isinstance.__dict__[storage_name]=value;    #跳过特性 防止递归
            else:
                raise ValueError('value must>0')
        return property(qty_gettter,qty_setter) #构建自定义对象
class LineItem:
    weight=quantity('weight')   #使用工厂函数自定义特性         #weight特性 覆盖了weight实例属性 因此对self.weight 或nutemeg.weight的每个引用  都有特性函数处理 
    price=quantity('price')    #同上
    def __init__(self,description,weight,price):    #
        self.description=description;
        self.weight=weight;
        self.price=price;
    def subtotal(self):
        return self.weight*self.price;
        
mutmeg=LineItem('Molumccan nutmeg',8,13.95);
print(mutmeg.price,mutmeg.weight);
print(vars(mutmeg).items())






