'''
894. 所有可能的满二叉树




题目描述
评论 (32)
题解(11)New
提交记录
满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。

返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。

答案中每个树的每个结点都必须有 node.val=0。

你可以按任何顺序返回树的最终列表。


'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N not in Solution.memo:
            ans = []
            for x in range(1,N+2,2):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]
a=Solution();
a.allPossibleFBT(7);


