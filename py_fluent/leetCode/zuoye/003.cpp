/*
    3 寻找节点中的最大值
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
int findMax(){
    int max=-1;		//保存最大值  -1为假设的一个默认最小值  此处可以尽可能小
    LNode *p=A;
    
    if(p==NULL){
        printf("此链表为空");
        return -1;
    }
    while (p->next)
    {
        if(p->next->data>=max){		//如果大于 最大值  max就变成当前值
            max=p->next->data;
        }
        p=p->next;
    }
    return max;
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
    cout<<"请输入链数据"<<endl;
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
    cout<<"最大值:"<<findMax();
	return 0;
}