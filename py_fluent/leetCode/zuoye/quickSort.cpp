#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

template<class T>
void quickSorted(T nums[],int left,int right){
    T temp=nums[left];
    int low=left;
    int height=right;
    if(left>=right)return;
    while (left<right){
        while(nums[right]>=temp && left<right){
            --right;
            break;
        }
         nums[left]=nums[right];
        while(nums[left]<=temp && left<right){

            ++left;
            break;
        }
         nums[right]=nums[left];
    }
    nums[left]=temp;
    quickSorted(nums,low,left);
    quickSorted(nums,left+1,height);
}

int main(){
    char nums[]="asdjhkiuqowe";
    quickSorted(nums,0,11);
    for_each(nums,nums+11,[](auto &x){cout<<x; });
}
