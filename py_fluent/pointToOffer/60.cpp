#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<double> twoSum(int n) {
        int nums[12][11 * 7] = { 0 };
        for (int i = 1; i <= 6; i++) {
            nums[1][i] = 1;
        }
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= 6 * i; j++) {
                for (int k = 1; k <= 6; k++) {
                    if (j - k <= 0)break;
                    nums[i][j] += nums[i - 1][j - k];
                }
            }
        }
        int all = pow(6, n);
        vector<double>vcs;
        for (int i = n; i <= n * 6; i++) {
            vcs.push_back(nums[n][i] /double(all));
        }
        return vcs;
    }
};
int main() {
    Solution a;
    a.twoSum(2);
}