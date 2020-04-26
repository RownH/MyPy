class Solution {
public:
    vector<int> singleNumbers(vector<int>& nums) {
        int state=0;
        for(auto &i:nums){
            state ^=i;
        }
        state&=(-state);
        int res1=0;
        int res2=0;
        for(auto &i:nums){
            if((state & i)==0){
                res1^=i;
            }else{
                res2^=i;
            }
        }
        vector<int>temp;
        temp.push_back(res1);
        temp.push_back(res2);
        return temp;
    }
};