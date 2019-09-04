'''
2.3 元组不仅仅是不可变的列表
 元组: 作用 不可变的列表  没有字段名的记录
 
 2.3.1 
 元组中每个元素都存放了记录的一个字段的数据,外加这个字段的位置
 因为是一个字段的集合  所以数量和位置信息非常重要
 元组的基本操作

 2.3.2 元组的拆包
 元组的拆包可以应用到任何可迭代对象上,唯一的要求是,被迭代对象中的元素要跟接受对象的一致,除非用*来处理多余的元素
 用*处理剩下的元素

 嵌套元组拆包  支持嵌套

 2.3.4 具名元组
 collection.namedtuple 是一个工厂函数,构建一个带字段名的数组和一个有名字的类

 2.3.5 作为不可变的元组
 除了增减操作之外,元组支持其他所有方法 
 不支持替换 更改 排序
 值不可变,顺序不可变
'''
from collections import namedtuple
def example27():
    lax_coordinates=(33.9425,-118.408056)
    city,year,pop,chg,area=('Tokyo',2003,32450,0.66,8014)
    traveler_ids=[('USA','A'),('USB',2),('ESB','3')]
    for _ in sorted(traveler_ids):
        print('%s %s'%_)
    for country,_ in traveler_ids:#元组的拆包
        print(country)

def example28():
    a,b,*rest=range(5) #*代表剩余部分组成元组
    print(a,b,rest)

def example29():
    metro_areas=[
        ('Tq','JP',36,(35,139)),
        ('dn','in',21,(28,77)),
        ('MC','MX',20,(19,-99)),
        ('NY','US',20,(40,-74)),
    ]   #嵌套的数组对象
    for name,cc,pop,(latitude,longitude) in metro_areas:
        if longitude<=0:
            print(name,cc,pop,latitude,longitude)

def example30():
    #定义和使用具名数组
    City=namedtuple('City','name country population coordinates')
    toky=City('Tokyo','Jp',36,(35.68,139.69))
    print(toky)
    print(toky.name) #直接访问
    print(toky[0])  #通过字段名或者位置访问
    #toky[0]='hello' #不可变列表
    print(toky._asdict()) #实例方法
    print(City._fields)#返回类型名
    for key,value in toky._asdict().items(): #遍历元组的方法
        print('%s : %s'%(key,value))
example27()
example28()
example29()
example30()