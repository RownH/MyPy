'''
94. 二叉树的中序遍历




题目描述
评论 (310)
题解(90)New
提交记录
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[];
        rlist=[];
        node=root;
        while node or len(stack)!=0:
            while node:
                stack.append(root)
                node=node.left;
            node=stack.pop()
            rlist.append(node);
            node=node.right
        return rlist;
        10
       5  15
          6 20  