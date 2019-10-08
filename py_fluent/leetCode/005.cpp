/*
    1 删除两个范围中的值
 */

#include<iostream>
#include<malloc.h>
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
        if(p->next->data>=i &&p->next->data<=k){
            temp=p->next;			//当下一个节点处于范围内,保存当前下一个节点信息
			p->next=p->next->next;	//当前节点的下一个节点 等于下下个节点.指针指向下下个节点   temp保存的节点不在A链中
			free(temp);	//释放temp指向节点
		}
        
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
    deleteRange(1,11);
	return 0;
}