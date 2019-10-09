/*
    2 将两个非递减的有序链表合为一个非递增的有序列表
    (要求利用原来两个链表的储存空间,不另外占用其他内存,表中不允许出现重复数据)
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

    cout<<"请输入第二条链数据"<<endl;
    getline(cin,line);
    stringstream str1(line);
    while (str1>>temp) {
            LNode *tmp= (LNode*)malloc(sizeof(LNode));
            tmp->next=NULL;
            tmp->data=temp;
            t2->next=tmp;
            t2=t2->next;
        }
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