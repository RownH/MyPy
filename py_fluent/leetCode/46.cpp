/*
46. 全排列
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
*/
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int> >res;
        if(n==1){
            res.push_back(nums);
            return res;   
        }
        vector<int>vc(n, 0);
        vector<int>temp;
        for (int i = 0; i < n; i++) {
            temp.push_back(nums[i]);
            dfs(i, n, vc, temp, nums, res);
            temp.pop_back();
        }
        return res;
    }
    void dfs(int i, int n, vector<int>vc, vector<int>one, const vector<int>& old, vector<vector<int> >& nums) {
        vc[i] = 1;
        for (int j = 0; j < n; j++) {
            if (vc[j] == 0) {
                one.push_back(old[j]);
                if (one.size() == n) {
                    nums.push_back(one);
                    return;
                }
                dfs(j, n, vc, one, old, nums);
                one.pop_back();;
            }
        }
    }
};