/*
54. 螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
*/
#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.size() == 0) {
            return vector<int>(0);
        }
        else if (matrix.size() == 1) {
            return matrix[0];
        }
        int left = 0, top = 0;
        int bottom = matrix.size() - 1;
        int right = matrix[0].size() - 1;
        vector<int>rel;
        while (left <=right && top <= bottom) {
            for (int i = left; i <= right; i++) {
                rel.push_back(matrix[top][i]);
            }
            for (int i = top+1; i <= bottom; i++) {
                rel.push_back(matrix[i][right]);
            }

            if (left < right && top < bottom) {
                for (int i = right-1; i > left; i--) {
                    rel.push_back(matrix[bottom][i]);
                }
                for (int i = bottom; i > top; i--) {
                    rel.push_back(matrix[i][left]);
                }
            }
            left++;
            bottom--;
            top++;
            right--;
        }
        return rel;
    }
};
int main() {
    Solution a;
    vector <vector<int> > b{ { 1,2,3,4},{5,6,7,8},{9,10,11,12}};
    auto c=a.spiralOrder(b);
    for (auto d : c) {
        cout << d << " ";
    }
}