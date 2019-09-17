'''
    5.9 函数注解
    python3提供一种句法 用于函数申明中的参数的返回值附加元数据
    
'''
from inspect import signature
def example591(text:str,max_len:'int >0' =80) ->str:  #有注解的函数声明 函数声明在各个参数都可以在:之后增加注解表达式,如果参数有默认值 放入参数名和默认值质检
    """在max_len前面或后面的第一个空格截断文本      #如果想注解某个返回值 在函数声明末尾的:之间添加->和一个表达式.那个表达式可以是任意类型的
    """                                        #{'text': <class 'str'>, 'max_len': 'int >0', 'return': <class 'str'>} 类似这样
    end=None;                                   #很使用的代码解释功能
    if len(text)>max_len:
        space_befor=text.rfind(' ',0,max_len);
        if space_befor>=0:
            end=space_befor;
        else:
            space_afeter=text.rfind(' ',max_len);
            if space_afeter>=0:
                end=space_afeter;
    if end is None:
        end=len(text)
    return text[:end];
print(example591.__annotations__)
print(signature(example591).return_annotation)
print(signature(example591).parameters.values())    #可解析提取 注解