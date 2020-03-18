class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        unordered_map<char,int>chart_table;
        int res=0;
        for(const auto  &i:chars){
            ++chart_table[i];
        }
        for(auto &i:words){
            unordered_map<char,int>word_table;
            for(auto &j:i){
                word_table[j]+=1;
            }
            int flag=0;
            for(auto &j:i){
                if(word_table[j]>chart_table[j]){
                    flag=1;
                    break;
                }
            }
            if(!flag){
                res+=i.length();
            }
        }
        return res;
    }
};