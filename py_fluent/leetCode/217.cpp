    #include<iostream>
    #include<set>
    #include<vector>
    using namespace std;
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> values;
        for (auto num : nums) {
            values.insert(num);
        }
        return nums.size() != values.size();
    }
};
int main()
{
    Solution a=Solution();
    vector<int>nums={1,2,3,1};
    a.containsDuplicate(nums);
    return 0;
}