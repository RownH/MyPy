
 //Definition for a binary tree node.
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };
 
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        dfs(root);
        return MAX;
    }
    int dfs(TreeNode *root){
        if(!root){
            return 0;
        }
        int left=dfs(root->left);
        int right=dfs(root->right);
        int max=left+right+1;
        if(MAX<max){
            MAX=max;
        }
        return left>right?left+1:right+1;
    }
private:
    int MAX=0;
};