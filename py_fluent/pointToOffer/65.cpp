class Solution {
public:
    int add(int a, int b) {
        while(b!=0){
            int temp=(unsigned)(b&a)<<1;
            a^=b;
            b=temp;
        }
        return a;
    }
};