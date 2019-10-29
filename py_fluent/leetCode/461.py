'''
461. 汉明距离




题目描述
评论 (299)
题解(80)New
提交记录
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。
'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1');
a=Solution();
print(a.hammingDistance(1,4));