'''
5.6 函数的内省
    使用dir函数可以探知factorial具有下列的属性
    ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__',
    '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '
    __hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__',
    '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    大部分属性时python对象共有的,所以我们把函数作为对象相关的属性 先从dict开始
    函数使用__dict__属性存储赋予他的用户属性,这相当于一种形式的解
    
    常用内省函数介绍
    __annotations__  参数和返回值的注解
    __call__ 可调用协议 ()运算符重载
    __closure__ 函数闭包 即自由变量的绑定
    __code__ 编译称字节嘛的函数元数据和函数定义体
    __defaults__ 形式参数的默认值
    __Get__ 实现只读描述符协议
    __global__ 函数所在模块中的全局变量
    __kwdefaults__ 仅现关键字形式参数的默认值
    __name__    函数名称
    __qualname__ 函数限定的名称 
'''
def fa():
    pass;
print(dir(fa))