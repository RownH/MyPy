/*
题目描述
评论 (128)
题解(266)
提交记录
面试题 01.01. 判定字符是否唯一
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

输入: s = "leetcode"
输出: false 
示例 2：

输入: s = "abc"
输出: true
限制：

*/

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