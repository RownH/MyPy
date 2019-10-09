/*
    1 删除两个范围中的值
 */

#include<stdio.h>
#include<malloc.h>
#include<iostream>
#include<sstream>
using namespace std;
typedef struct LNode{
    int data;
    LNode *next;
}LNode;
LNode *A, *B, *C;
void deleteRange(int i,int k){
    LNode *p=A;//指向A头节点
    if (p==NULL)
    {
        printf("当前为空");
        return;
    }	//如果A为空  直接退出
    LNode *temp;
    while (p->next)  //判断p是否有下一个节点
    {
        if(p->next->data>i &&p->next->data<k){
            temp=p->next;			//当下一个节点处于范围内,保存当前下一个节点信息
            p->next=p->next->next;	//当前节点的下一个节点 等于下下个节点.指针指向下下个节点   temp保存的节点不在A链中
            free(temp);	//释放temp指向节点
        }else {
            p=p->next;
        }

    }

}
void createLinkList(){
    //初始化链表
    LNode *t1, *headA;
    LNode *t2, *headB;
    A = (LNode*)malloc(sizeof(LNode));
    B = (LNode*)malloc(sizeof(LNode));
    t1 = A;
    headA = A;
    t2 = B;
    headB = B;
    A->next = NULL;
    B->next = NULL;
    int temp;
    string line;
    cout<<"请输入第一条链数据"<<endl;
    getline(cin,line);
    stringstream str(line);
    while (str>>temp) {
            LNode *tmp= (LNode*)malloc(sizeof(LNode));
            tmp->next=NULL;
            tmp->data=temp;
            t1->next=tmp;
            t1=t1->next;
        }
}
int main(void){
    createLinkList();
    cout<<"请输入i值和j值";
    int i,j;
    if(cin>>i>>j)deleteRange(i,j);
    LNode *p=A;
    cout<<"删除后:"<<endl;
    while (p->next)
    {
        cout<<p->next->data<<" ";
        p=p->next;
    }

    return 0;
}
