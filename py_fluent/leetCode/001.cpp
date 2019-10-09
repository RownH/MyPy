/*
    1 将两个非递减的有序链表合为一个非递减的有序列表
    (要求利用原来两个链表的储存空间,不另外占用其他内存,表中不允许出现重复数据)
 */
#include<stdio.h>
#include<malloc.h>
using namespace std;
typedef struct LNode{
	int data;
	LNode *next;
}LNode;			//定义链表
LNode *A, *B, *C;		//全局变量  A,B为将合并的链头   C合成后的链表头
void merge(LNode *A, LNode *B, LNode *&C){
	LNode *p = A->next;			//头节点下一个  头节点默认为0  不在范围内
	LNode *q = B->next;			// 保存B头节点 以后的链 同上
	LNode *r;	
	LNode *temp;			//释放重复节点内存				
	C = A;					//利用A链头 作为合并之后的头   不占有其他内存
	C->next = NULL;			
	free(B);				//释放B头空间  现在只需要使用到A头
	r = C;					//r指针指向C头节点
	while(p != NULL && q != NULL){  	//A链当前节点和B链当前节点不为空时
		if(p->data <= q->data){    //如果A链当前节点<=B链当前节点   此情况 C链 应该添加A链当前节点
            if(p->data==q->data){	//当A链当前节点 =B链当前节点时   
				temp=q;
			    q=q->next;    		//为了去重复  B链节点下移
				free(temp);		//释放重复节点内存
			}
            r->next = p;		//添加A链当前节点 在C链末尾
			p = p->next;		//A链当前节点下移
			r = r->next;		//C链移到末尾
    
		}
		else{
			r->next = q;	//当A链当前节点>B链当前节点  应该加入B链当前节点
			q = q->next;	//同上
			r = r->next;
		}
	}
	r->next = NULL;		//C链末尾置为空
	if(p != NULL){		//如果A链比B链长   那么剩下 将A链后面节点直接添加到C末尾
		r->next = p;
	}
	if(q != NULL){		//同理
		r->next = q;
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
	while(p->next != NULL){		//忽略头节点
		printf("%d ", p->next->data);
		p = p->next;
	} 
	return 0;
}