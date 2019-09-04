'''
切片 
适用于list tuple str这类序列类型都支持切片操作

2.41  为什么切片和区间会忽略最后一个元素
 以0为起始下标的传统
 
 用法list[x:y]
 当省略时不写

2.42 对对象进行切片
 形式 s[a:b:c]对s在a,b区间之间以c个间隔
 python在使用slice(a,b,c)时,c为负值时表示反向取值
 对seq[start:stop:step]进行求值的时候,python会调用seq.__getItem__(slick(a,b,c)) 就算不自己定义序列类型

 2.43 多维切片和省略
 []运算符还可以使用以都好分开的多个索引或者切片
 二维的numpy.ndarray就可以用a[i,j]抑或a[m:n,k:l]的方式进行二维切片
 2.44 给切片赋值

'''
def example21():
    l=[10,20,30,40,50,60,70];1
    print(l[:2])
    print(l[2:])
    print(l[:3])
    print(l[::2])
    print(l[::-1])#反向取值
    print(l[::-2])#反向间隔为2
    l[3:5]=[1]
    print(l)
    l[2:5]=[-2,-1,0,1,2,3] #多退少补  多的添加在后面  少的不用修改
    print(l)

example21()


