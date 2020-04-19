class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if(nums.size()==0)return 0;
        int n=nums[0];
        int count=1;
        for(int i=1;i<nums.size();i++){
            if(nums[i]==n){
                ++count;
            }else{
                --count;
                if(count<0){
                    n=nums[i];
                    count=1;
                }
            }
        }
        return n;
    }
};