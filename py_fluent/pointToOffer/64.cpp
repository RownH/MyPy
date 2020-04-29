class Solution {
public:
    int sumNums(int n) {
        res+=n;
        int x=n>0&& sumNums(n-1);
        return res;
    }
    int res=0;
};