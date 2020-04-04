/*
面试题09. 用两个栈实现队列
*/
#include<iostream>
#include<string>
#include<vector>
using namespace std;
class Solution {
public:
    bool isUnique(string astr) {
        if (astr.size() == 0)return 1;
        int state = 0;
        for (int i = 0; i < astr.size(); i++) {
            int newState = 1 << (astr[i] - 'a');
            
            if ((state & newState )== newState) {
                return false;
            }
            else {
                state |= newState;
            }
        }
        return true;
    }
};
int main() {
    Solution  a;
    a.isUnique("leetcode");
}