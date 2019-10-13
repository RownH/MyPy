'''
349. 两个数组的交集




题目描述
评论 (351)
题解(55)New
提交记录
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]
说明:

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1=set(nums1)
        set2=set(nums2)
        if len(set1)>len(set2):
            return list(set1 and set2);
        else:
            return list(set2 and set1);