/*
16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
*/
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int min = 1000;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            int j = i + 1;
            int k = nums.size() - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (abs(target - sum) < abs(target - min)) {
                    min = sum;
                }
                if (sum < target) {
                    j++;
                    while (j <= k && nums[j] == nums[j - 1]) {
                        j++;
                    }
                }
                else if (sum > target) {
                    k--;
                    while (k >= j && nums[k] == nums[k +1]) {
                        k--;
                    }
                }
                else {
                    return target;
                }
            }
        }
        return min;
    }
};