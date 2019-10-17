'''
412. Fizz Buzz




题目描述
评论 (123)
题解(25)New
提交记录
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
'''
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lists=[];
        for i in range(1,n+1):
            lists.append(self.size(i))
        return lists;
    def size(self,n):
        if n%3==0 and n%5==0:
            return 'FizzBuzz';
        elif n%3==0:
            return 'Fizz';
        elif n%5==0:
            return 'Buzz';
        else:
            return str(n);
s=Solution();
print(s.fizzBuzz(2));