#include <iostream>
#include<string>
#include<math.h>
#include<stdio.h>
using namespace std;
inline bool isNumber(const char& c){

    if( c=='0' ||c=='1' || c=='2' || c=='3' ||c=='4' ||c=='5' || c=='6' || c=='7' || c=='8' || c=='9'){
        return true;
    }
    return false;
}
inline int Number(const char& c){
    switch (c) {
        case '0':
            return 0;
        case '1':
             return 1;
        case '2':
            return 2;
        case '3':
            return 3;
        case '4':
            return 4;
        case '5':
            return 5;
        case '6':
            return 6;
        case '7':
            return 7;
        case '8':
            return 8;
        case '9':
            return 9;
    }
}
inline char NumberToChar(const int& c){
    switch (c) {
        case 0:
            return'0';
        case  1 :
             return '1';
        case  2 :
            return'2';
        case  3 :
            return'3';
        case  4 :
            return'4';
        case  5 :
            return'5';
        case  6 :
            return'6';
        case  7 :
            return'7';
        case  8 :
            return'8';
        case  9 :
            return'9';
    }
}
inline bool isComma(const char& c){
    if(c==','){
        return true;
    }
    else{
        return false;
    }
}
class node{
public:
    node(int data,node * prePtr=nullptr,node *nextPtr=nullptr):N(data),pre(prePtr),next(nextPtr){

    }

public:
    int N; //整数
    node * next;
    node * pre;
};
class myList{
public:
    myList(const string & s,bool S=true):symbol(S){
        int i=0;
        if(s[i]=='-'){
            symbol=0;
            ++i;
        }else if(s[i]=='+'){
            symbol=1;
            ++i;
        }
            listlength=0;
            int n=0;//记录累计多少次无逗号
            headNode=new node(-1);
            trailNode=headNode;

            for (;i<s.length();i++) {
                if(isNumber(s[i])){
                    node *temp=new node(Number(s[i]),trailNode);
                    trailNode->next=temp;
                    trailNode=trailNode->next;
                    ++n;
                    ++listlength;
                    if(n>4){
                        cerr<<"每隔4个数字 应该有,隔开"<<endl;
                    }
                }
                else if(isComma(s[i])){
                    if(n<4){
                        if(listlength<4){
                            n=0;//重置
                            continue;
                        }
                        else{
                            cerr<<"此处应该有4个数字"<<endl;
                            exit(0);
                        }
                    }
                    else if(n==4){
                        n=0;//重置
                        continue;
                    }
                    else{
                        cerr<<"此处前只有4个数字"<<endl;
                         exit(0);
                    }

                }else{
                    cerr<<"异常"<<endl;
                     exit(0);
                }


        }
    }
    ~myList(){
        node *p=headNode;
        node *q=headNode;
        while (p) {
            q=p->next;
            p->pre=nullptr;
            delete  p;
            p=q;
        }
    }
    static myList  addTwo(const myList &lhs,const myList& rhs,bool S=1){
        node *p,*q;
       if(lhs.listlength>rhs.listlength){
        p=lhs.trailNode;
        q=rhs.trailNode;
       }
       else {
        p=rhs.trailNode;
        q=lhs.trailNode;
       }    //p为长度较长的一端
        string res;
       int temp=0;
       char charTemp;
       while (q->N!=-1) {
          temp=p->N+q->N+temp;
          if(temp>=10){
             temp-=10;
             charTemp=NumberToChar(temp);
            res=charTemp+res;
            temp=1;
          }
          else{
             charTemp=NumberToChar(temp);
             res=charTemp+res;
             temp=0;
          }
          q=q->pre;
          p=p->pre;
       }

       while (p->N!=-1) {
            temp=p->N+temp;
            if(temp>=10){
                temp-=10;
                charTemp=NumberToChar(temp);
                temp=1;

            }
            else{
            charTemp=NumberToChar(temp);
            temp=0;
            }
            res=charTemp+res;
            p=p->pre;
       }
       string resStr;
       int N=res.size()/4;
       int Y=res.size()%4;

       int i=0;
       if(Y!=0){
           for (;i<Y;i++) {
              resStr=res[i];
           }
           resStr+=',';
       }
       for (i=0;i<N;i++) {
           string temp="";
           for (int j=0;j<4;j++) {
               temp+=res[i*4+j+Y];
           }
           temp=i==N-1? temp:temp+",";
           resStr=resStr+temp ;
       }


       return myList(resStr,S);
    }
    static::myList  subTwo(const myList &lhs,const myList& rhs,bool S=1){
        node *p,*q;
       if(lhs.listlength>rhs.listlength){
        p=lhs.trailNode;
        q=rhs.trailNode;
            S=lhs.symbol;
       }
       else if(lhs.listlength==rhs.listlength){
           p=lhs.headNode->next;
           q=rhs.headNode->next;
           bool compare=1;
           while (p &&q) {
               if(p->N>q->N){
                    compare=1;
                   break;
               }
               else if (p->N==q->N) {
                   p=p->next;
                   q=q->next;
                   continue;
               }
               else {
                    compare=0;
                    break;
               }
           }
           if(compare){
               p=lhs.trailNode;
               q=rhs.trailNode;
               if(lhs.symbol==rhs.symbol){
                   S=1;
               }
               else
               S=lhs.symbol;
           }else{
               p=rhs.trailNode;
               q=lhs.trailNode;
               if(lhs.symbol==rhs.symbol){
                   S=1;
               }
               else
               S=rhs.symbol;
           }

       }
       else {
        p=rhs.trailNode;
        q=lhs.trailNode;
        S=rhs.symbol;
       }    //p为长度较长的一端
        string res;
        int temp=0;
        char charTemp;
        while (q->N!=-1) {
           temp=p->N-q->N+temp;
           if(temp<0){
              temp+=10;
              charTemp=NumberToChar(temp);
             res=charTemp+res;
             temp=-1;
           }
           else{
              charTemp=NumberToChar(temp);
              res=charTemp+res;
              temp=0;
           }
           q=q->pre;
           p=p->pre;
        }

        while (p->N!=-1) {
             temp=p->N+temp;
             if(temp<0){
                 temp+=10;
                 charTemp=NumberToChar(temp);
                 temp=-1;

             }
             else{
             charTemp=NumberToChar(temp);
             temp=0;
             }
             res=charTemp+res;
             p=p->pre;
        }
        string resStr;
        int N=res.size()/4;
        int Y=res.size()%4;

        int i=0;
        if(Y!=0){
            for (;i<Y;i++) {
               resStr=res[i];
            }
            resStr+=',';
        }
        for (i=0;i<N;i++) {
            string temp="";
            for (int j=0;j<4;j++) {
                temp+=res[i*4+j+Y];
            }
            temp=i==N-1? temp:temp+",";
            resStr=resStr+temp ;
        }
        return myList(resStr,S);
    }
    myList  operator +(const myList& other){
        if(this->symbol==1 && other.symbol==1){
               return addTwo(*this,other);
        }
        else if(this->symbol==0 &&other.symbol==0){
               return addTwo(*this,other,0);
        }
        else if(this->symbol==1 &&other.symbol==0){
            return subTwo(*this,other);
        }
        else{
             return subTwo(*this,other);
        }
    }
    myList  operator -(const myList &other){
        if(this->symbol==1 && other.symbol==1){
               return subTwo(*this,other,0);
        }
        else if(this->symbol==0 &&other.symbol==0){
               return subTwo(*this,other,0);
        }
        else if(this->symbol==1 &&other.symbol==0){
            return addTwo(*this,other,1);
        }
        else{
             return addTwo(*this,other,0);
        }
    }
    void display()const {
        int y=listlength%4;
        int z=listlength/4;
        int i=0;
        string res="";
        node *ptr=headNode->next;
        if(y!=0){
            for (;i<y;i++,ptr=ptr->next) {
                res+=NumberToChar(ptr->N);

            }
            res=listlength<4 ? res:res+',';
        }
        for (i=0;i<z;i++) {
            string temp="";
            for (int j=0;j<4;j++,ptr=ptr->next) {
                temp+=NumberToChar(ptr->N);
            }

            res+=i==z-1 ?temp: temp+',';
        }
        res=symbol==0?'-'+res:res;
        cout<<res<<endl;
    }

private:
    bool symbol;//1 正号  0负号
    node * headNode;//头节点
    node * trailNode;//尾节点
    int listlength;//链表长度
};
int main()                    //主函数
    {
     cout<<"|===============================================|"<<endl;
     cout<<"|***********************************************|"<<endl;
     cout<<"|**********欢迎使用任意长整数加减法系统**************|"<<endl;
     cout<<"|***********************************************|"<<endl;
     cout<<"|***********************************************|"<<endl;
     cout<<"|在此系统中，可以输入任意长的整数 。               |"<<endl;
     string ch;
     char Yes_No;
     do{
      cout<<"|输入形式为：(-)**,****,****|"<<endl;
      cout<<"|即符号+数，每4位加一个','|"<<endl;
      string strA;
      string strB;
      int op;
      cout<<"请输入第一个数："<<endl;
      cin>>strA;
      cout<<"请输入第二个数："<<endl;
      cin>>strB;
      cout<<"请输入操作类型 1 加法 2 减法"<<endl;
      cin>>op;
      if(op==1){
          myList C{myList(strA)+myList(strB)};
          C.display();
      }
      else if(op==2){
          myList C{myList(strA)-myList(strB)};
          C.display();
      }else{
          cerr<<"错误类型"<<endl;
      }

      cout<<"是否继续计算(Y/N):";                  //询问是否继续计算
      cin>>Yes_No;
     }while(Yes_No=='y'||Yes_No=='Y');   //Yes_No不等于'Y'或'y'时，程序退出
     cout<<"|===============================================|"<<endl;
     cout<<"|***********************************************|"<<endl;
     cout<<"|*****************感谢使用本系统!***************|"<<endl;
     cout<<"|***********************************************|"<<endl;
    return 1;
}
