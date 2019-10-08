/*
    2 将两个非递减的有序链表合为一个非递增的有序列表
    (要求利用原来两个链表的储存空间,不另外占用其他内存,表中不允许出现重复数据)
 */

#include<iostream>
#include<malloc.h>
using namespace std;
typedef struct LNode{
	int data;
	LNode *next;
}LNode;
LNode *A, *B, *C;
void merge(LNode *A, LNode *B, LNode *&C){
	LNode *p = A->next;
	LNode *q = B->next;
	LNode *r;
    LNode *temp;
	C = A;
	C->next = NULL;
	free(B);
	r = C;
	while(p != NULL && q != NULL){
		if(p->data <= q->data){		//同理
            if(p->data==q->data){
                temp=q;				//保存当前B链重复指针
				q=q->next;   		//B链节点下移 
				free(temp);		//删除B链
            }
            temp=p;			//记录当前A链节点
            p = p->next;	//A链当前节点下移
            temp->next=r;	//将C链前面加入当前A链节点
            r=temp;			//C链头节点上移
		}
		else{
            temp=q;
            q=q->next;
            temp->next=r;
            r=temp;
		}
	}

    while (p!=NULL)		//将剩余的节点 追加在头节点上
    {
            temp=p;
            p = p->next;
            temp->next=r;
            r=temp;
    }
    while (q!=NULL)
    {
            temp=q;
            q=q->next;
            temp->next=r;
            r=temp;
    }
    C=r;
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
	A5->data = 5;
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
	
	LNode *B2 = (LNode*)malloc(sizeof(LNode));
	B2->data = 2;
	LNode *B4 = (LNode*)malloc(sizeof(LNode));
	B4->data = 3;
	LNode *B6 = (LNode*)malloc(sizeof(LNode));
	B6->data = 6;
	LNode *B8 = (LNode*)malloc(sizeof(LNode));
	B8->data = 7;
	B8->next = NULL;
	
	t2->next = B2;
	t2 = t2->next;
	t2->next = B4;
	t2 = t2->next;
	t2->next = B6;
	t2 = t2->next;
	t2->next = B8;
    
}
int main(void){
	createLinkList();
	merge(A, B, C);
	LNode *p = C;

	while(p->next != NULL){
		printf("%d ", p->data);
		p = p->next;
	} 
	return 0;
}