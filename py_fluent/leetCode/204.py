'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

厄拉多塞筛法:
    从2开始  如果2为质数 那么之后的每一个2的倍数都是复数
    以此地推
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=[True]*n;
        count=0
        for i in range(2,n):
            if nums[i]:
                count+=1;
            for _ in range(i,n,i):
                nums[_]=False;
        return count;
