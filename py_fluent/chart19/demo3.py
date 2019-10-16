'''
    特性全解析
    虽然property经常作为装饰器
    但是他其实是一个类

    在python中 类和汉书常可以互换,因为两者都是可调用的对象,而且没有实例化的
    new运算符,所以调用构造方法与调用工厂汉书没有区别
    只要能返回新的可调用对象 代替被装饰的汉书 二者都可以用作装饰器

    property构造方法的完整签名:
    property(fget=None,fset=None,fdel=None,doc=None)
    所有参数都是可选的,如果没有把函数传给某个某个参数,那么得到的特性对象就不允许
    执行相应的操作

'''
class LineItem:
    def __init__(self,description,weight,price):
        self.description=description;
        self.weight=weight;
        self.price=price;
    
    def subtotal(self):
        return self.weight*self.price;
    
    def get_weight(self):
        return self.__weight;
    
    def set_weight(self,value):
        if value>0:
            self.weight=value;
        else:
            raise ValueError('value must >0')
    weight=property(get_weight,set_weight,'weight in kilograms')    #特性文档
    #在方法众多的类定义体内 使用装饰其器的话,一眼就能看出那些是读值方法  那些是设置方法
    

    #观点  从obj.attr这样的表达式不会从obj开始寻找attr,而是从obj.__class__开始,而且当类中没有名为attr的特性时
    #python才会在obj实例中 寻找,这条规则不仅使用于特性,还适用于整类描述符 覆盖型描述符
class Class:
    data='the class data attr'
    @property
    def prop(self):
        return 'the prop value'
obj=Class()
print(vars(obj)) #表示实例对象属性为空
print(obj.data)
obj.data='bar';
print(vars(obj)) #实例对象添加 遮盖类属性
print(Class.data)# 类对象

print(Class.prop)
print(obj.prop)
#obj.prop='foo'; #不能设置
obj.__dict__.update({obj.prop:'fpp'});
print(vars(obj))
print(obj.prop);#仍没有被覆盖
Class.prop='baz';#被覆盖  销毁特性对象
print(obj.prop);#出现异常  并未被销毁
print(help(LineItem))
'''
特性的文档 控制台中的help()函数或IDE等工具需要显示特征的文档时
会从特性的__doc__属性中提取信息
'''


            

