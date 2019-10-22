'''
    434. 字符串中的单词数

题目描述
评论 (177)
题解(23)New
提交记录
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

输入: "Hello, my name is John"
输出: 5
'''
class Solution:
    def countSegments(self, s: str) -> int:
        s=s.strip(' ');
        if s=='':
            return 0;
        dicts=s.split(' ');
        print(dicts)
        return len([_ for _ in dicts if _!=''])
a=Solution();
print(a.countSegments(", , , ,        a, eaefa"))