'''
    处理属删除操作
    python中 对象的属性可以使用del语句删除
    其实不常删除属性,通过特性删除更少见.
    @my_property.delteter装饰其包装一个方法  负责删除特性管理属性
'''
class BlackKnight:
    def __init__(self):
        self.members=['an arm','anthor arm','a leg','anther leg'];
        self.phrases=["This but a scratch.",
            "It's just a flesh wound.",
            "I'am in vincible!",
            "ALlright,we'll call it a draw."]
    @property 
    def member(self):
        print('next member is:')
        return self.members[0]

    @member.deleter
    def member(self):
        text='BLACK KNIGHT(loses {}) n--{}'
        print(text.format(self.members.pop(0),self.phrases.pop(0)))

kneight=BlackKnight();
print(kneight.member)
del kneight.member