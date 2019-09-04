'''
    2.7 list.sorted操作和内置函数sorted
    list.sorted 会就地排序 返回值为None 缺点  无法形成连贯的接口
    sirted排序结果为新的对象
    reverse: 为True时 排序对象降序输出
    默认为False;
    Key:一个只有一个参数的函数,这个函数会被用在序列中的每一个元素,所产生的结果是排序算法的对比关键字

    2.8 用bisect来管理已排序的序列
    bitsect(haystack,needle)在haystack中搜索needle的位置,该位置满足的条件时 插入后仍保持升序 haystack必须时一个有序的序列
    先通过bisect查找index
    在通过haystack,insert(index,needle)插入新值,也可以一步到位
'''
import bisect
import sys
HAYSTACK=[1,4,5,6,8,12,15,20,21,23,23,26,29,30]
NEDDLE=[0,1,2,5,8,10,22,23,29,30,31]
def demo(bisect_fn):
    for neddle in reversed(NEDDLE):
        position=bisect_fn(HAYSTACK,neddle)
        bisect.insort(HAYSTACK,neddle)
        print(HAYSTACK)

bisect_fn=bisect.bisect_left;
print(bisect_fn.__name__)
print(' '.join('%2d' %n for n in HAYSTACK))
demo(bisect_fn)

