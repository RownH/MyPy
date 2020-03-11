
#include<iostream>
#include<vector>
#include<queue>
using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int> >result;
        int i, j, k = 0;
        int count;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0)break;
            if (i > 0 && nums[i] == nums[i - 1])continue;
            j = i + 1;
            k = nums.size()-1;
            while (j < k) {
                count = nums[i] + nums[j] + nums[k];
                if (count > 0) {
                    k--;
                }
                else if (count < 0) {
                    j++;
                }
                else {
                    vector<int>temp;
                    temp.push_back(nums[i]);
                    temp.push_back(nums[j]);
                    temp.push_back(nums[k]);
                    result.push_back(temp);
                    while (j<k && nums[j]==nums[j+1])
                    {
                        j++;
                    }
                    while (j<k && nums[k] == nums[k-1])
                    {
                        k--;
                    }
                    j++;
                    k--;
                }
            }

        }
        return result;
    }
};
int main() {
    Solution a;
    vector<int>temp{ 0,2,1,-6,6,-7,9,1,2,0,1 };
    a.threeSum(temp);
}