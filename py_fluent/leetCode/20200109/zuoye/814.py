class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def ifRegex(node):
            if node is None:
                return 0
            left=ifRegex(node.left)
            right=ifRegex(node.right);
            if left==0:
                node.left=None;
            if right==0:
                node.right=None;
            return node.val or left or right;
        ifRegex(root);
        return root;