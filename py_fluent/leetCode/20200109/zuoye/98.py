'''
98. 验证二叉搜索树




题目描述
评论 (399)
题解(84)New
提交记录
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root,low=float('-inf'),height=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True;
        if not low<root.val<height:
            return False;
        return self.isValidBST(root.left,low,root.val) and self.isValidBST(root.right,root.val,height);
        