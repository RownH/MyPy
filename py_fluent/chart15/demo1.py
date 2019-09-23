'''
    with语句会设置一个临时的上下文,交给上下文管理器对象控制,负责清理上下文,这么做能避免错误并减少样板代码
    除了自动关闭文件之外,还有其他用途

    try:
        当仅当try语句快没有异常抛出时才运行else块,else子句抛出的异常不会由前面的except字句处理

    15.2 上下文管理器和with块
    上下文管理器对象存在的目的时管理with语句,就像迭代器的存在是为了惯了for语句一样

    with 语句的目的是简化try/finaly模式.这周哦你模式用于保证一段代码运行完毕后执行某项操作
    即便那段代码由于异常,即便让你语句或sys.exit()调用而终止.finally通常用于释放重要的资源

    上下文管理器:
        __enter__  
        __exit__
    执行with后的表达式得到的结果是上下文管理器对象,不过把值绑定到目标变量上 时在上下文管理器对象上调用__enter__方法的结果
    不论什么方式退出都会在上下文管理对象中调用__exit__退出
    
    with语句上的as字句时可选的,对open函数来说,必须加上as字句,以便获取文件的引用,不过有些上下文管理器会返回NOnde,因为没有什么返回的

    15.3 contextlib模块中的实用工具

    closing 
        如果对象提供了close()方法,但是没有实现__enter__ 或者__exit__协议  可以使用这个函数构建上下文管理器
    
    suppress
        构建临时忽略指定异常的上下文管理器

    @contextmanager
        这个装饰器把简单的生成器函数变成上下文管理器,不用创建类取实现管理器协议

    conntexDecorator
        这是个基类,用于定义基于类的上下文管理器.这种上下文管理器也能用于装饰函数,在管理的上下文中运行整个函数
    
    ExitStack
        这个上下文管理器能进入多个上下文管理器.with块借宿时 exitStack按照后进显出的顺序调用栈中各个上下文管理器的__exit__方法.如果事先不知道with块
        要进入多少个上下文管理器,可以使用这个类

    15.4 使用@contextmanager
    减少上下文管理器的样板代码量,因为不用编写一个完整的类,定义了__enter__和__exit__方法.
    只需要有一个yield语句的生成器,生成让__enter__方法返回的值

    在使用@contextmanagment装饰的生成器中,yield语句的作用是把函数的定义体分成两部分:yield
    语句前面的所有代码在with块开始,yield后面的代码在__enter__结束时执行

'''

class LookingGlass:
    def __enter__(self):
        import sys;
        self.original_write=sys.stdout.write;
        sys.stdout.write=self.reverse_write;
        return 'JABBERWOCKY'
    def reverse_write(self,text):
        self.original_write(text[::-1]);
    def __exit__(self,exc_type,exc_value,traceback):
        import sys
        sys.stdout.write=self.original_write
        if exc_type is ZeroDivisionError:
            print('plase DO NOT divide bu zero !')
            return True;
def example151():
    with LookingGlass() as what:
        print('Alice,Kitty and Snowdrop')
        #print(what)
def example152():
    manage=LookingGlass()
    print(manage)
    monster=manage.__enter__();
    print(monster); #此时还是正常的
    print(monster=='JABBERWOCKY')
    manage.__exit__(None,None,None);
    print(monster)  #关闭后 返回正常

import contextlib
@contextlib.contextmanager
def example153():
    import sys
    original_write=sys.stdout.write

    def reverse_write(text):
        return original_write([::-1])
    sys.stdout.write=reverse_write
    yield 'JAVVERWORCKY'        #若在此抛出异常,则永远无法恢复
    sys.stdout.write=self.original_write; #contextlib.contextmanager装饰器报称实现__enter 和__Exit__方法的类
                                          #__exter__方法有如下作用  调用生成器函数,保存生成器对象  调用next 执行到yield关键字所在的位置
                                         #返回next(gen)产出的值,以便把产出的值绑定到with/as语句中的目标变量上
                                         
                                         #with终止时 __exit__会执行 检查有没有把异常传给exc_type 如果有,调用gen.throw.  否则调用next 继续执行生成器函数定义体中yield语句之后的代码

    #如果__exit__返回True 此时解释器为压制异常,如果__exit__没有显示返回一个值  那么解释器是None 然后向上冒泡异常.
    #使用contexmanager装饰器时,,默认行为时相反,如果不想contexmanager压制异常,需要显示抛出异常\

example152()

