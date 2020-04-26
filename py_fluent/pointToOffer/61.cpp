class Solution {
public:
    bool isStraight(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int size=0;
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]==0){
                size++;
            }
            else if(nums[i]==nums[i+1]){
                return false;
            }
        }
        return nums.back()-nums[size]<5;

    }
};