'''
414. 第三大的数
题目描述
评论 (268)
题解(35)New
提交记录
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:

输入: [3, 2, 1]

输出: 1

解释: 第三大的数是 1.
示例 2:

输入: [1, 2]

输出: 2

解释: 第三大的数不存在, 所以返回最大的数 2 .
示例 3:

输入: [2, 2, 3, 1]

输出: 1
'''
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums);
        nums=sorted(list(nums))
        if len(nums)==0:
            return 0;
        if len(nums)==1:
            return nums.pop();
        elif len(nums)==2:
            return nums.pop();
        else:
            return nums[-3]


