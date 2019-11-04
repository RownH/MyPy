'''
965. 单值二叉树




题目描述
评论 (168)
题解(28)New
提交记录
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。

 

示例 1：



输入：[1,1,1,1,1,null,1]
输出：true
示例 2：



输入：[2,2,2,5,2]
输出：false
 

提示：

给定树的节点数范围是 [1, 100]。
每个节点的值都是整数，范围为 [0, 99] 。

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isLeftEqRight(root):
            if root is None:
                return True;
            if root.left or root.right :
                if root.left and root.right is None:
                    return root.val==root.left.val and isLeftEqRight(root.left) ;
                elif root.right and root.left is None:
                    return root.val==root.right.val  and isLeftEqRight(root.right) ;
                else:
                    return root.left.val==root.right.val and root.right.val==root.val and  isLeftEqRight(root.left) and isLeftEqRight(root.right)
            return True;
        return isLeftEqRight(root);