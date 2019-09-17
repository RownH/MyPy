'''
    5.7 从定位参数到仅限关键字参数
    python提供了极为灵活的参数处理机制
    python3 进一步提供了仅限关键字.
    函数使用*和** 展开可迭代的兑现,映射到单个参数
    

'''

def tag(name,*content,cls=None,**attrs):
    if cls is not None:
        attrs['class']=cls;
    if attrs:
        attr_str=''.join('%s="%s"' %(attrs,value)  for attrs,value in sorted(attrs.items()))
    else:
        attr_str='';
    if content:
        return '\n'.join('<%s %s>%s</%s>'%(name,attr_str,c,name) for c in content)
    else:
        return '<%s %s/>'%(name,attr_str);

def f(a,*,b):
    return a+b;
print(tag('br'))
print(tag('p','hello'))
print(tag('p','hello','word','name',cls="id"))
print(tag(content='name',name='img'))
m_tag={'name':'img','title':'Sunset' }  #参数展开
print(tag(**m_tag))
#print(f(1,2));#错误测试  b必须指定名字
print(f(1,b=2)); 