class Solution {
public:
    int findMin(vector<int>& nums) {
        int left=0;
        int right=nums.size()-1;
        int middle=0;
        while(left<right){
            middle=(left+right)/2;
            if(nums[right]<nums[middle]){//右边无序
                left=middle+1;
            }
            else{
                right=middle;
            }
        }
        return nums[right];
    }
};
