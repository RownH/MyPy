/*
面试题04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

*/
class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        int n=0;
        int m=0;
        if(matrix.size()>0){
            n=matrix.size();
            m=matrix[0].size();
        }
        int i=m-1;
        int j=0;
        while(true){
            if(j>=n || i<0){
                return false;
            }
            if(matrix[j][i]>target){
                --i;
            }
            else if(matrix[j][i]<target){
                ++j;
            }
            else{
                return true;
            }
        }
        return false;
    }
};
