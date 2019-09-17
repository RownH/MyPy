#include<iostream>
#include<vector>
using namespace std;
int Turn(int num){
    string temp=to_string(num);
    for(int i=0;i<temp.size();i++){
        if(temp[i]=='0' ||temp[i]=='1' ||temp[i]=='8')
        {
            continue;
        }
        else if(temp[i]=='2')
        {
            temp[i]='5';
        }
        else if(temp[i]=='5')
        {
            temp[i]='2';
        }
        else if(temp[i]=='6')
        {
            temp[i]='9';
        }
        else if(temp[i]=='9')
        {
            temp[i]='6';
        }
        else{
            return -1;
        }
    }
    return stoi(temp);
}
int main(){
    int x;
    cin>>x;
    int count=0;
    for(int i=1;i<=x;i++){
        int turanI=Turn(i);
        if(turanI!=-1 & turanI!=i){
            count++;
        }
    }
    cout<<count;
    return 0;
}
