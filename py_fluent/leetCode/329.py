'''
326. 3的幂




题目描述
评论 (203)
题解(23)New
提交记录
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？
'''
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=0;
        j=0;
        while j<n:
            j=3**i;
            i+=1;
            if j==n:
                return True;
        return False;
c=Solution();
print(c.isPowerOfThree(9))