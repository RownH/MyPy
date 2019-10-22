'''
429. N叉树的层序遍历
题目描述
评论 (129)
题解(36)New
提交记录
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
例如，给定一个 3叉树 :
返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]
说明:
树的深度不会超过 1000。
树的节点总数不会超过 5000。
'''
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        stack=[root];
        result=[];
        while stack:
            data=[obj.val for obj in stack]
            son=[];
            for _ in stack:
                for j in _.children:
                    son.append(j);
            stack=son;
            result.append(data);
        return result;



