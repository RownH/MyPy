'''
979. 在二叉树中分配硬币




题目描述
评论 (35)
题解(10)New
提交记录
给定一个有 N 个结点的二叉树的根结点 root，树中的每个结点上都对应有 node.val 枚硬币，并且总共有 N 枚硬币。

在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。(移动可以是从父结点到子结点，或者从子结点移动到父结点。)。

返回使每个结点上只有一枚硬币所需的移动次数。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cns=0;
        def dfs(node):
            if node is None:
                return 0;
            l,r=dfs(node.left),dfs(node.right);
            self.cns+=abs(l)+abs(r);
            return node.val+l+r-1;
        dfs(root);
        return self.cns