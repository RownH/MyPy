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
    int kthLargest(TreeNode* root, int k) {
        stack<TreeNode*>m_stk;
        TreeNode *cur=root;
        vector<int>m_vc;
        while(m_stk.size()>0 || cur){
            while(cur){
                m_stk.push(cur);
                cur=cur->left;
            }
            cur=m_stk.top();
            m_vc.push_back(cur->val);
            m_stk.pop();
            cur=cur->right;
        }
        return *(m_vc.end()-k);
    }
    
};