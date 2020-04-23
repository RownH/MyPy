class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n=nums.size();
        int left=0;
        int right=n-1;
        while(left<=right){
            int middle=left+((right-left)>>1);
            if(middle==nums[middle]){
                left=middle+1;
            }
            else{
                right=middle-1;
            }
        }
        return left;
    }
};