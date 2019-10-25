'''
448. 找到所有数组中消失的数字




题目描述
评论 (187)
题解(46)New
提交记录
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]

'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def swap(nums, n1, n2):
            if n1!=n2:
                nums[n2]=nums[n2]^nums[n1];
                nums[n1]=nums[n1]^nums[n2];
                nums[n2]=nums[n2]^nums[n1];
        for _ in range(len(nums)):
            while nums[_]!=nums[nums[_]-1]:
                swap(nums,_,nums[_]-1)
                print(nums)
        return [num+1 for num in range(len(nums)) if num!=nums[num]-1]
a=Solution();
a.findDisappearedNumbers([8,7,6,5,4,3,2,1])#打印