/*
    4  逆序
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
void reverse(){
    LNode *p,*q,*r;	
    if(A==NULL)return ;
    q=A;	//A指向当前头节点
    p=NULL;	//P指向空节点
    while (q)	// 3个指针   一个保存下一个节点 ,一个保存当前节点,一个保存上一个节点. 保证链接不会断开
    {
        r=q->next;//r保存 当前节点的下一个		
        q->next=p;//当前节点指向前一个节点
        p=q;	//前一个节点 向后移动
        q=r;	//当前节点向后移动一个节点
    }
	cout<<"逆序后:"<<endl;
    while (p->next)
    {
		cout<<p->data<<" ";
        p=p->next;
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
    reverse();

	return 0;
}