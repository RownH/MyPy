'''
    342. 4的幂




题目描述
评论 (140)
题解(25)New
提交记录
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false
'''
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<0:
            return False
        if num==1:
            return True;
        if num<4:
            return False
        if num==4:
            return True
        snum=str(bin(num))
        index=len(snum)-snum.find('1')-2
        snum[len(snum)-snum.find('1')-2]='0';
        if int(snum)==0:
            if index%3==0:
                return True
        else:
            return False;
c=Solution();
c.isPowerOfFour(16);