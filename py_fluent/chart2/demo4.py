'''
切片 
适用于list tuple str这类序列类型都支持切片操作

2.41  为什么切片和区间会忽略最后一个元素
 以0为起始下标的传统
 
 用法list[x:y]
 当省略时不写

2.42 对对象进行切片
 形式 s[a:b:c]对s在a,b区间之间以c个间隔
 python在使用slice(a,b,c)时
'''
def example21():
    l=[10,20,30,40,50,60,70];
    print(l[:2])
    print(l[2:])
    print(l[:3])
    print(l[::2])



example21()


