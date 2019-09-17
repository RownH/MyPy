'''
    5.8 获取参数的信息

    __defalult__属性 他的值是一个元组,里面保存着定位参数和关键字参数的默认值
    仅限关键字参数的默认值保存在__kwdefaults__属性中
    参数的名称保存在__code__中
'''

def clip(text,len=80):
    a=len;

print(clip.__defaults__)    #默认参数
print(clip.__code__)
print(clip.__code__.co_varnames)    #不包括默认参数
print(clip.__code__.co_argcount)    