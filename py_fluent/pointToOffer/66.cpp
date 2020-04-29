class Solution {
public:
    vector<int> constructArr(vector<int>& a) {
        int n = a.size();
        vector<int>res(n, 0);
        int left = 1;
        for (int i = 0; i < n; i++) {
            res[i] = left;
            left = a[i] * left;
        }
        int right = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] = res[i] * right;
            right *= a[i];
        }
        return res;
    }
};