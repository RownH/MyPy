/*
    4  逆序
 */

#include<iostream>
#include<malloc.h>
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
        
    while (p->next)
    {
       printf("%d ",p->data);
        p=p->next;
    }
}
void createLinkList(){
	// headA与headB是用来调试的 
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
	
	LNode *A1 = (LNode*)malloc(sizeof(LNode));
	A1->data = 1;
	LNode *A3 = (LNode*)malloc(sizeof(LNode));
	A3->data = 3;
	LNode *A5 = (LNode*)malloc(sizeof(LNode));
	A5->data = 11;
	LNode *A7 = (LNode*)malloc(sizeof(LNode));
	A7->data = 7;
	LNode *A9 = (LNode*)malloc(sizeof(LNode));
	A9->data = 9;
	A9->next = NULL;
	t1->next = A1;
	t1 = t1->next;
	t1->next = A3;
	t1 = t1->next;
	t1->next = A5;
	t1 = t1->next;
	t1->next = A7;
	t1 = t1->next;
	t1->next = A9;
	t1 = t1->next;
	

    
}
int main(void){
	createLinkList();
    reverse();

	return 0;
}