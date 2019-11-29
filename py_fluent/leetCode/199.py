'''199. 二叉树的右视图




题目描述
评论 (190)
题解(60)New
提交记录
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''
#方法 DFS 或者 BFS 
#下述方法代码较短
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        d = {}
        def f(r, i):
            if r:
                d[i] = r.val
                f(r.left, i + 1)
                f(r.right, i + 1)
        f(root, 0)
        return d.values()