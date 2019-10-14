'''
    使用shelve 模块调整OSCON数据源的结构
    19.1.4 使用shelve模板调整OSCON数据源的结构
    shelve架子
    pickle泡菜  对象序列化格式的名字 还是在那个格式与对象之间互相转换的某个模块的名字
    shelve.open高阶函数返回一个shelve.shelf实例

    shelve.Shelf是abc.MutableMapping的子类 因此提供了处理映射类型的重要方法
    shelv.Shelf类还提供了几个管理I/O的方法.
'''
import warnings
import shelve
import inspect
import demo1
DB_NAME='shcedule1_db'
CONFERENCE='conference.115'
class Record:
    def __init__(self,**kwargs):#允许传入0或任意个参数 
        self.__dict__.update(kwargs)    #使用关键字参数传入属性构建实例的方式
    def __eq__(self,other):
        if isinstance(other,Record):
            return self.__dict__==other.__dict__
        else:
            return NotImplemented;

class DbRecored(Record):
    __db=None;
    @staticmethod
    def set_db(db):
        DbRecored.__db=db;
    
    @staticmethod
    def get_db():
        return DbRecored.__db;
    
    @classmethod
    def fetch(cls,ident):
        db=cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                msg="database not set; call '{}.set_db(mydb)'"
            else:
                raise
    def __repr__(self):
        if hasattr(self,'serial'):
            cls_name=self.__class__.__name__;
            return '<{} serial={!r}>'.format(cls_name,self.serial)
        else:
            return super().__repr__();
def load_db(db):
    raw_data=demo1.load();
    warnings.warn('loading' +DB_NAME)
    for collection,rec_list in raw_data['Schedule'].items():#迭代集合
        record_type=collection[:-1] #去掉后缀s
        for record in rec_list:
            key='{}.{}'.format(record_type,record['serial'])#构建key
            record['serial']=key
            db[key]=Record(**record)#构建数据库的key建下
class Event(DbRecored):
    @property 
    def venue(self):
        key='venve.{}'.format(self.venue_serial)
        return self.__class__.fetch(key)
        
db=shelve.open(DB_NAME)
if CONFERENCE not in db:
    load_db(db)
spearker=db['speaker.3471'] #   解决数字问题
DbRecored.set_db(db);
event=DbRecored.fetch('event.33950');
print(event.venue)
db.close()