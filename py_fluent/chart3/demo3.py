'''
    3.4  硬件的弹性键查询
    为了方便 当我们某个键的映射不存在时,我们希望可以得到一个默认值
    方法  使用defultdict或者自定义dict子类 实现__missing__方法
    
    3.4.1 defultdict 处理找不到的键的一个选择
    需要在用户构建的时候配置一个找不到键的默认方法
    会在__getitem__找不到时返回某种默认值

    比如 dd=defaultdict(list);
    dd['new_key']
    步骤 调用list创造一个新的列表
    把这个列表作为值,'new-key'放在其中
    返回这个列表的引用

    3.4.2 特殊方法__missing__
    当所有的映射类型在处理找不到的键的时候,都会牵扯到__missing__泛噶非,dict没有定义这个方法,但是提供了这个方法的接口
    也就时说 一个类继承dict 如果找不到键时,就会调用他  而不是抛出错误


'''
class StrKeyDict0(dict):
    def __missing__(self,key):
        if isinstance(key,str):     #此测试是必须的 否则将无穷递归
            raise KeyError(key) #第一次没找到 ,且类型为str时,则抛出异常
        return self[str(key)]   #如果类型不为str,则转化为str后在进行get
    
    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return default;
    
    def __contains__(self,key):
        return key in self.keys() or str(key) in self.keys()
d=StrKeyDict0([('2','two'),('4','four')]);
print(d[2])
print(d.get('2'),d.get('3'))    #使用get时 会调用missing 方法  而[]不会