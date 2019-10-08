/*
    3 寻找节点中的最大值
 */

#include<malloc.h>
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
    printf("%d",findMax());

	return 0;
}