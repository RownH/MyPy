class Solution {
public:
    int search(vector<int>& nums, int target) {
        int right=find_first_height(nums,target);
        if(right==-1)return 0;
        int left=find_first_low(nums,target);
        return  find_first_height(nums, target)-find_first_low(nums, target)+1;
    }

    int find_first_low(vector<int>nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (nums[middle] < target) {
                left = middle + 1;
            }
            else if (nums[middle] > target) {
                right = middle - 1;
            }
            else {
                if (middle == 0 || nums[middle - 1] != target)return middle;
                else {
                    right = right - 1;
                }
            }
        }
        return -1;
    }
    int find_first_height(vector<int>nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (nums[middle] < target) {
                left = middle + 1;
            }
            else if (nums[middle] > target) {
                right = middle - 1;
            }
            else {
                if (middle == nums.size()-1 || nums[middle + 1] != target)return middle;
                else {
                    left = left + 1;
                }
            }
        }
        return -1;
    }
};
int main(){


    
}