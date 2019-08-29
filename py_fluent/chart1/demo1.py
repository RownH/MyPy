'''
Python的数据类型

python风格  len(collection) 而不是collection.len()

这种设计思想体现在Python的数据模型上,而数据模型所描述的API,为构建对象提供工具
数据模型时对python接口的规范.

python解释器碰到特殊句法时,会使用特殊方法去激活一些基本的对象操作,这些特殊方法的名字以两个下划线开头 类似与C++ 基本运算符的重载  在此基础上有更好的深入
类似与
m[key] 解释器实际调用m.__getitem__(key)
通过特殊方法名可以实现:

迭代
集合类
属性访问
运算符重载
函数和方法的调用
对象的创建和销毁
字符串表示形式和格式化
管理上下文

1.1 magic and dunder
    魔术方法也称dunder 双下方法,是特殊方法的昵称

'''
import collections
from random import choice
#随机选取
Card=collections.namedtuple('Card',['rank','suit',])
#构建简单的类来表示一张纸牌 
#namedtuple 用以构建少数属性但是没有方法的对象
class FrenchDeck:
    rank=[str(n) for n in range(2,11)]+list('JQKA')
    suits='Spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards=[Card(rank,suit) for suit in self.suits
                                    for rank in self.rank
                                    ]
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]
def spader_high(card):
    rank_value=FrenchDeck.rank.index(card.rank)
    return rank_value+len(suit_values)+suit_values[card.suit]

deck=FrenchDeck();
print(len(deck))
beer_card=Card('7','diamonds')
print(beer_card)
print(deck[0])
print(deck[-1])
print(choice(deck))
#随机选择数组中的一个

print(deck[:3])
#支持切片
print(deck[3::-1])
#支持反向迭代操作
print(Card('Q','hearts') in deck)
#__contains__ 如果未显示实现,模式顺序查找的方式
suit_values=dict(Spades=3,hearts=2,diamonds=1,clubs=0)
print(sorted(deck,key=spader_high))