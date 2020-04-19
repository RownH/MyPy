/*
面试题27. 二叉树的镜像

*/
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* mirrorTree(TreeNode* root) {
        if(root==NULL)return root;
        TreeNode *left=root->left;
        TreeNode *right=root->right;
        root->left=right;
        root->right=left;
        mirrorTree(left);
        mirrorTree(right);
        return root;
    }

};