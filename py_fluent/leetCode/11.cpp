/*
盛水最多得容器
11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。
*/
class Solution {
public:
    int maxArea(vector<int>& height) {
        int *p=&height[0];
        int *q=&height[height.size()-1];
        int max=0;
        while(p<q){
            int *min=*p>*q?q:p;
            int m=(q-p)*(*min);
            max=max>m?max:m;
            *p>*q?--q:++p;
        }
        return max;
    }
};