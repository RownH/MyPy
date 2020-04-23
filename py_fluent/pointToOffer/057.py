class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int left=0;
        int right=nums.size()-1;
        vector<int>temp;
        while(left<=right){
            int sum=nums[left]+nums[right];
            if(sum==target){

                temp.push_back(nums[left]);
                temp.push_back(nums[right]);
                return temp;
            }
            else if(sum<target){
                ++left;
            }
            else{
                --right;
            }
        }
        return temp;
    }
};