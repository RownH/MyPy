/*
945. 使数组唯一的最小增量
给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。

返回使 A 中的每个值都是唯一的最少操作次数。

示例 1:

输入：[1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
示例 2:

输入：[3,2,1,2,1,7]
输出：6
解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
*/
#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int minIncrementForUnique(vector<int>& A) {
        int max = 0;
        for (int i = 0; i < A.size(); i++) {
            if (A[i] > max) {
                max = A[i];
            }
        }
        max = max > A.size() ? max : 2 * A.size();
        vector<int>B(2 * max + 1, -1);
        int count = 0;
        for (int i = 0; i < A.size(); i++) {
            if (B[A[i]] == -1) {
                B[A[i]] = 1;
            }
            else {
                for (int j = A[i] + 1; j < 2 * max; j++) {
                    count++;
                    if (B[j] == -1) {
                        B[j] = 1;
                        break;
                    }
                }
            }
        }
        return count;
    }
};
int main() {
    Solution a;
    vector<int>b = { 3,2,1,2,1,7 };
    a.minIncrementForUnique(b);
    
}