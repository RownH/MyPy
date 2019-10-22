'''
    20.2  覆盖型与非覆盖型描述符对比
    Python的存取属性方式不对等
    通过实例读取属性时,返回的是实例中定义的熟悉,如果实例没有指定属性,那么会获取类属性.而为实例赋值时,通常会在实例中创建属性

    根据是否定义__set__ 描述符可以分为两大类,


'''
def cls_name(obj_or_cls):
    cls=type(obj_or_cls)
    if cls is type:
        cls=obj_or_cls;
    return cls.__name__.split('.')[-1]

def display(obj):
    cls=type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None),int]:
        return repr(obj)
    else:
        return '<{}> object'.format(cls_name(obj));

def print_args(name,*args):
    pseudo_args=','.join(display(x) for x in args)
    print('-> {}.__{} __({})'.format(cls_name(args[0]),name,pseudo_args));

class Overriding:   #有set和get
    def __get__(self,instance,owner):
        print_args('get',self,instance,owner)
    
    def __set__(self,instance,value):
        print_args('set',self,instance,value);
class OverridingNotGet:
    def __set__(self,instance,value):
        print_args('set',self,instance,value);

class NonOverriding:
    def __get__(self,instance,owner):
        print_args('get',self,instance,owner)

class Managed:#托管类
    over=Overriding();  #覆盖型实例
    over_no_get=OverridingNotGet()#覆盖型没有get
    non_over=NonOverriding()
    def spm(self):
        print('-> Managed.spam({})'.format(display(self)))    
obj=Managed()
print(obj.over) #obj.over触发描述符的__get__方法,第二个参数的托管实例是obj
print(Managed.over)#触发描述符的__get__方法,第二个参数为None
obj.over=7;#触发set 最后一个参数为7
print(obj.over)# 读取obj.over 仍会触发描述符的__get__方法
print(vars(obj))    #实例中 并没有参数
print(vars(Managed))
obj.__dict__['over']=8;
print(vars(obj))
print(obj.over)#仍然Managed.over仍会覆盖


# 没有get的方法 
'''
    因为没有处理读操作的__get__方法.如果直接通过实例的__dict__属性创建同名实例属性,以后在设置那个属性.就会直接从实例中返回新赋予的值
    而不会返回描述符对象.也就是说,实例属性会遮盖描述符,不过只有读操作如此.

'''

print(obj.over_no_get)
print(Managed.over_no_get)
obj.over_no_get=7
obj.__dict__['over_no_get']=9;

print(obj.over_no_get)
print(Managed.over_no_get)
obj.__dict__['over_no_get']=9;
print(vars(obj))