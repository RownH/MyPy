'''
    20.3 如果方法是描述符
    在类中定义的函数属于绑定方法
    因为用户定义的函数都有__get__方法.所以依附在类上时,就相当于描述符


from demo3 import Managed;
obj=Managed();
print(obj.spm)  #获得绑定方法的对象
print(Managed.spm)#获得函数
obj.spm=7;  #遮盖类属性
print(obj.spm)  #没有实现__set__ 因此是非覆盖型描述符
#通过托管类访问,函数的__get__方法会返回自身的引用  但是通过实例 __get__返回的是绑定方法对象
'''
import collections
class Text(collections.UserString):

    def __repr__(self):
        return 'Text({ ! r })'.format(self.data)
    def reverse(self):
        return self[::-1];

word=Text('forword');
print(word)
print(word.reverse())
print(Text.reverse(Text('hello')))
print(type(word),type(Text.reverse)) #一个类属性  一个方法
print(Text.reverse.__get__(word))
print(Text.reverse.__get__(none,Text))
