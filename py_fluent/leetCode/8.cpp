#include<iostream>
#include<string>
using namespace std;
class Solution {
public:
    int myAtoi(string str) {
        int res = 0;
        int fuShu = 0;
        int nums = 0;
        int firstChar = 0;
        if (str.size() == 0)return 0;
        for (int i = 0; i < str.size(); i++) {
            if (str[i] == ' ') {
                if (nums > 0) {
                    break;
                }
                continue;
            }
            if (str[i] == '-' && fuShu == 0) {
                fuShu = -1;
                continue;
            }
            if (str[i] == '+' && fuShu == 0) {
                fuShu = 1;
                continue;
            }
            else if ('0' <= str[i] && str[i] <= '9') {
                if (fuShu * res > INT_MAX / 10) {
                    return INT_MAX;
                }
                if (fuShu * res < INT_MIN / 10) {
                    return INT_MIN;
                }
                res = res * 10 + (str[i] - '0');
                nums++;
            }
            else {
                if (nums == 0) {
                    return 0;
                }
                else {
                    break;
                }
            }
        }
        return fuShu == 0 ? res : fuShu * res;
    }

};
int main() {
    string str = "-2147483648";
    Solution a;
    a.myAtoi(str);
}