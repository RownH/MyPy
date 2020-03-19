/*
面试题49. 丑数
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
*/
class Solution {
public:
    int nthUglyNumber(int n) {
        int dp2=0,dp3=0,dp5=0;
        int *nums=new int[n];
        nums[0]=1;
        for(int i=1;i<n;i++){
            nums[i]= min(nums[dp2]*2,min(nums[dp3]*3,nums[dp5]*5));
            if(nums[i]==nums[dp2]*2){
                dp2++;
            }
            if(nums[i]==nums[dp3]*3){
                dp3++;
            }
            if(nums[i]==nums[dp5]*5){
                dp5++;
            }
        }
        return nums[n-1];
    }
};  