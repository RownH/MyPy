'''
    第6章 使用一等函数实现设计模式

    6.1 重构策略模式

    6.2 选择最佳策略
'''
from abc import ABC,abstractclassmethod #抽象类
from collections import namedtuple 

Customer=namedtuple('Customer','name fidelity')
class LineItem:
    def __init__(self,product,quanlity,price):
        self.product=product;
        self.quanlity=quanlity;
        self.price=price;
    
    def total(self):
        return self.price*self.quanlity;

class Order:
    def __init__(self,customer,cart,promotion=None):
        self.customer=customer;
        self.cart=list(cart)
        self.promotion=promotion;
    def total(self):
        if not hasattr(self,'__total'):
            self.__total=sum(item.total() for item in self.cart)
            return self.__total;
        
    def due(self):
        if self.promotion is None:
            discount=0
        else:
            discount=self.promotion.discount(self)
        return self.total()-discount;

    def __repr__(self):
        fmt='<Order total:{:. 2f} due: {:. 2f}>'
        #return fmt.format(self.total(),self.due())
        return str(self.total());
'''
class Promotion(ABC): #抽象基类
    @abstractclassmethod
    def discount(self,order):
        pass
class FidelityPromo(Promotion):
    def discount(self,order):
        return order.total()*0.05 if order.customer.fidelity>=1000 else 0

class BulkItemPromo(Promotion):
    def discount(self,order):
        discout=0;
        for item in order:
            if item.quanlity>=20:
                discout+=item.total()*0.1
        return discout;
'''
def fidelity_promo(order):
    '''积分1000以上的顾客提供%5的折扣 '''
    return order.total()*.05 if order.customer.fidelity>=1000 else 0
#使用函数实现折扣系统
def bulk_item_promo(order):
    '''单个商品为20个或以上时提供%7的折扣'''
    discount=0
    for item in order.cast:
        if item.quanlity>=20:
            discount+=item.total() *0.1
    return discount;

def large_order_promo(order):
    distinct_items={item.product for item in order.cast}
    if len(distinct_items)>=0:
        return order.total()*0.07
    return 0



promos=[globals()]
#模块是一等对象,标准库提供了几个处理模块的函数,Python文档时这样说明内置函数的
#返回一个字典,表示当前的全局符号表,这个符号始终针对当前模块
def best_promo(ord):
    pass
Joe=Customer('John Doe',0)
ann=Customer('Ann Simith',1100)
cart=[LineItem('banana',4,5),
                LineItem('apple',10,1.5),
                LineItem('watermellon',5,5.0)
                ]
print(Order(Joe,cart,fidelity_promo))

