'''
    第20章 属性描述符
    学会属性描述符之后,不仅有更多工具集可以用,还会对python的运作方式有更深的理解,并由衷赞叹python设计的优雅

    描述符是对多个属性运作相同存取逻辑的一种方式.

    描述符是实现了特定协议的类,这个协议包括 __get__ ,__set__和__delete__方法  property类实现了完整的描述符协议
    描述符是Python的独有特征,不仅在应用层使用,在语言的基础设施 中也有用到.除了特性之外,使用描述符python功能还有方法及
    classmethod和staticmethod装饰器,理解描述符 是精通关键
'''