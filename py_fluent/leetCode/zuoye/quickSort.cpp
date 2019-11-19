#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

template<class T> 
void quickSorted(T nums[],int left,int right){
    T temp=nums[left];
    int low=left;
    int height=right;
    while (left<right){
        while(nums[right]<temp && left<right){
            nums[left]=nums[right];
            --right;
        }
        while(nums[left]>temp && left<right){
            nums[right]=nums[left];
            ++left;
        }
    }
    nums[left]=temp;    
    for_each(nums,nums+6,[](auto a){cout<<a;});
    cout<<endl<<left<<right<<endl;
    // quickSorted(nums,low,left);
    // quickSorted(nums,left+1,height);
}

int main(){
    int nums[]={7,6,5,2,1,3};
    quickSorted(nums,0,5);
    for_each(nums,nums+6,[](auto a){cout<<a;});
}