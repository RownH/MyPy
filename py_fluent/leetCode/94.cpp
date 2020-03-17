/**
 * 94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//中序遍历
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode *>stk;
        vector<int>res;
        TreeNode *cur=root;
        while(!stk.empty() || cur!=NULL){
            while(cur){
                stk.push(cur);
                cur=cur->left;
            }
            cur=stk.top();
            stk.pop();
            res.push_back(cur->val);
            cur=cur->right;
        }
        return res;
    }
};
//前序遍历
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode *>stk;
        vector<int>res;
        TreeNode *cur=root;
        while(!stk.empty() || cur!=NULL){
            while(cur){
                res.push_back(cur->val);
                stk.push(cur);
                cur=cur->left;
            }
            cur=stk.top();
            stk.pop();
            cur=cur->right;
        }
        return res;
    }
};
//后序遍历
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        stack<TreeNode *>stk;
        vector<int>res;
        TreeNode *cur=root;
        while(!stk.empty() || cur!=NULL){
            while(cur){
                res.insert(res.begin(),cur->val);
                stk.push(cur);
                cur=cur->right;
            }
            cur=stk.top();
            stk.pop();
            cur=cur->left;
        }
        return res;
    }
};