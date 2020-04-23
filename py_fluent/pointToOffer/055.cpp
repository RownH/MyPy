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
    bool isBalanced(TreeNode* root) {
        return decur(root)!=-1;
    }
    int decur(TreeNode *root){
        if(root==NULL){
            return 0;
        }
        int lDeth=decur(root->left);
        if(lDeth==-1){
            return -1;
        }
        int rDeth=decur(root->right);
        if(rDeth==-1){
            return -1;
        }
        if(abs(lDeth-rDeth)<=1){
            return max(lDeth,rDeth)+1;
        }else{
            return -1;
        }
    }
};