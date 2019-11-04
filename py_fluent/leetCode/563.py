'''
563. 二叉树的坡度




题目描述
评论 (93)
题解(14)New
提交记录
给定一个二叉树，计算整个树的坡度。

一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

整个树的坡度就是其所有节点的坡度之和。

示例:

输入: 
         1
       /   \
      2     3
输出: 1
解释: 
结点的坡度 2 : 0
结点的坡度 3 : 0
结点的坡度 1 : |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1
注意:

任何子树的结点的和不会超过32位整数的范围。
坡度的值不会超过32位整数的范围。

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.tilt = 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traverse(root)
        return self.tilt

    def traverse(self, root):
        if root is None:
            return 0

        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.tilt += abs(left-right)
        return left+right+root.val