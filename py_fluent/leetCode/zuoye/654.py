# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root=TreeNode(0);
        def setNum(node,low,height):
            maxValue=max(nums[low:height]);
            maxValue=nums.index(maxValue)
            if height==maxValue:
                node=nums[maxValue];
            elif low==maxValue:
                node=nums[maxValue];

            setNum(node.left,low,maxValue);
            setNum(node.right,maxValue+1,height);
        setNum(root,0,len(nums));
        return root;
s=Solution();
s.constructMaximumBinaryTree([3,2,1,6,0,5]);