#include<iostream>
#include<string>
#include<fstream>
using namespace std;

string getStr(string path){
    ifstream in(path);
    if(!in){
        cout<<"不存在"<<path<<"文件"<<endl;
        return "";
    }
    else{
        string str;
        while (1)
        {
            char c=in.get();
            if(isupper(c)||isdigit(c)){
                str+=c;
            }
            else{
                if(!in.eof()){
                    cout<<"文件格式错误"<<endl;
                    return "";
                }else{
                    break;
                }
            }
        }
        if(str.length()>40){
            cout<<"字符最多为40个"<<endl;
            return "";
        }
        return str;
    }
}
string encode(string str){
    string estr="";
    for(int i=0;i<str.length();i+=2){
        if(!isupper(str[i])){
            cout<<"格式错误"<<str[i]<<"应该为大写"<<endl;
            return " ";
        }
        if(!isdigit(str[i+1])){
            cout<<"格式错误"<<str[i+1]<<"应该为数字"<<endl;
            return " ";
        }
        char c=str[i+1];
        const char *n=&c;
        for(int j=0;j<atoi(n);j++){
            estr+=str[i];
        }
    }
    return estr;
}
string uncode(string str){
    string ustr="";
    for(int i=0;i<str.length();){
        int count=1;
        for(int j=i+1;j<=str.length();j++){
            if(str[j]==str[i]){
                count++;
            }
            else{
                ustr+=str[i]+to_string(count);
                i=j;
                break;
            }
        }
    }
    return ustr;
}


int main(){
    cout<<"输入user:"<<endl;
    char user;
    cin>>user;
    if(user=='D'){
        string str=getStr("d.txt");
        cout<<str<<endl;
        string dstr=uncode(str);
        cout<<dstr;
    }else if(user=='E'){
        string str=getStr("e.txt");
        cout<<str<<endl;
        string estr=encode(str);
        cout<<estr;
    }else{
        cout<<"没有这个User"<<user<<endl;
    }
    
    return 0;
}