'''
    19.6处理属性的重要属性和函数
    Python为处理动态属性而提供的内置函数和特殊方法
    
    19.6.1 影响属性处理方式的特殊属性:
    __class__ 
        对象所属类的引用 obj.__class__ 与 type(obj)作用相同 Python中某些特殊方法 例如__getattr__ 只在类中找,不在实例中寻找

    __dict__
        一个映射,存储对象或类的可写属性
        有一个__dict__属性的对象,任何时候都能随意设置新属性.如果类有__slots__属性,
        那么他可能没有__dict__属性 
    
    __slots__
        
        类可以定义这个属性,限制实例可能有那些属性.__slots__属性值是一个字符串组成的元素,指明允许有那些属性
        如果__slots__中没有__dict_,那么该类的实例没有__dict__属性,实例只允许有制定名称的属性

        __slots__最好是元组 (不允许修改) 因为处理完定义体之后再修改__slots__列表没有任何作用




    19.6.2 处理属性的内置函数
    
    dir 
    列出对象的大多数属性 

    getattr
    从obj对象中获取name字符串对应的属性,获取的属性可能来自对象所属的类或超类
    如果没有指定的属性,getattr函数才抛出AttributeError异常

    hasattr
    如果obj对象中存在指定的属性,或者以某种方式 通过object对象获取制定的属性
    返回True  这个函数实现的方法是调用getattr 看看是否抛出异常

    setattr(obj,name,value)

    把object对象制定属性设为value 前提是obejct对象能接受那个值
    这个函数可能会创建一个新属性  或者覆盖现有属性

    vars
    返回obj对象的__dict__属性,如果实例所属类定义了 __slots__
    实例没有__dict__属性,那么vars属性不能处理,dir可以粗护理
    如果没有制定参数 那么vars()函数作用与local()函数一样 返回表示本地作用域的字典



    19.6.3   处理属性的特殊方法
    在用户自定义类中,下列特殊方法用于获取,设置,删除,和列出属性

    使用点号或内置的getattr,hasattr和setattr函数存取属性都会触发下述列表中相应的特殊方法.
    但是 直接通过案例的 __dict__属性读写不户处罚这些特殊方法

    特殊方法不会被实例属性覆盖

    通常 只要使用obj.attr
    或者obj.getattr(obj,'attr')
    都会触发class.__getattribute__(obj,'attr')
    方法


    __getattr__(self,name)
    仅当获取指定的属性失败,搜索过obj,Class和超类之后调用
    仅当找不到指定属性时才会处罚

    __getattribute__(self,name)
    尝试获取指定属性时会调用这个方法,不过寻找的属性是特殊属性或特殊方法时除外.
    点号与getattr和hasattr内置函数都会触发这个方法.
    抛出异常时 彩绘调用__getAttr__方法  为了在获取obj实例属性中不导致无限递归

    __setattr__
    尝试指定的属性时都会调用这个方法,点号与setattr内置函数都会触发这个方法


'''
print(vars())