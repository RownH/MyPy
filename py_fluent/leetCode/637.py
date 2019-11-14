'''
637. 二叉树的层平均值




题目描述
评论 (132)
题解(26)New
提交记录
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.

示例 1:

输入:
    3
   / \
  9  20
    /  \
   15   7
输出: [3, 14.5, 11]
解释:
第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        dfs=[];
        dfs.append(root);
        avergList=[];
        while dfs:
            newList=[];
            count=0.0
            nums=0;
            while dfs:
                tmp=dfs.pop();
                nums+=1;
                count+=tmp.val;
                if tmp.left:
                    newList.append(tmp.left);
                if tmp.right:
                    newList.append(tmp.right)
            avergList.append(count/nums);
            dfs=newList;
        return avergList



