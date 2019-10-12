'''
    19.1 使用动态属性转换数据

    如何使用动态属性访问JSON数据


    我们把__init__称为构造方法 用于构建实例的特殊方法__new__ 
     因为调用__init__方法时要传入要传入实例 ,而且禁止返回 任何值 
     所以init方法其实是初始化方法, 真正的构造方法是__new__.
     但是我们不用写__new__ 因为从Object类继承的实现已经足够

'''
from urllib.request import urlopen
import warnings
import os 
import json
import keyword
from collections import abc

URL='http://www.oreilly.com/pub/sc/osconfeed'
JSON='osconfeed.json'

def load():
    '''
    if not os.path.exists(JSON):
        
        msg='downloading {} to {}'.format(URL,JSON);
        warnings.warn(msg)
        with urlopen(URL) as remote,open(JSON,'wb') as local:
            local.write(remote.read());
    '''
    with open(JSON) as fp:
        return json.load(fp);
'''
class FrozenJSON:
    def __init__(self,mapping):
        self.__data={}
        for key,value in mapping.items():
            if keyword.iskeyword(key):
                key+='_'
            self.__data[key]=value   # 确定传入一个字典,创建副本

    def __getattr__(self,name): #当没有制定名称属性时,才调用__getattr__方法
        if hasattr(self.__data,name):       #如果name是__data的属性,返回那个属性
            return getattr(self.__data,name)
        else:
            return FrozenJSON.build(self.__data[name])  #否则 返回build结果
    
    @classmethod
    def build(cls,obj):
        if isinstance(obj,abc.Mapping): #如果obj是映射 那就构建一个FrozenJSON对象
            return cls(obj)                             
        elif isinstance(obj,abc.MutableSequence):   #如果是列表,构建一个列表
            return [cls.build(item) for item in obj]
        else:               #如果不是字典也不是一个列表,那么直接返
            return obj
        #缺陷  没有异常处理机制 无法处理关键字
        #__getattr__使用这个这个方法访问属性
        #使用__new__方法以灵活式创建对象 __init__称为构造方法 用于构造的实力是特殊方法__new__ 
'''
class FrozenJSON:
    '''
        用__new__和__init__修饰
    '''
    def __new__(cls,arg):       #__new__是类方法,第一个参数是类本身 余下的参数和__init__一样 
        if isinstance(arg,abc.Mapping):
            return super().__new__(cls);        #调用基类的类__new__方法 把唯一的参数 设置为FreozenJson 
                                                #等效 obj.__new__(FrozenJSON )
        elif isinstance(arg,abc.MutableMapping):    
            return [cls(item) for item in arg]
        else:
            return arg;
    
    def __init__(self,mapping):
        self.__data={}
        for key,value in mapping.items():
            if keyword.iskeyword(key):
                key+='_'
            self.__data[key]=value;
    
    def __getattr__(self,name):
        if hasattr(self.__data,name):
            return getattr(self.__data,name);
        else:
            return FrozenJSON(self.__data[name])    #之前使用的是build方法  现在直接使用构造方法
            
def object_maker(the_class,some_arg):
    new_object=the_class.__new__(some_arg)
    if isinstance(new_object,the_class):
        the_class.__init__(new_object,some_arg)
        return new_object;
feed_row=load()
feed=FrozenJSON(feed_row);  #构建列表
