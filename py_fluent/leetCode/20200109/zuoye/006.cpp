/*
    6 用栈和队列判断是否为回文字符串
 */
#include<stdio.h>
#include<malloc.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<sstream>
using namespace std;
//定义一个链栈  
typedef struct node
{
	char data;
	struct node * next;
}stacknode; //新节点
typedef stacknode * linkstack; //头节点
 
//定义一个链队列
typedef struct qnode
{
	char data;
	struct qnode * next;
}queuenode; //定义新节点
typedef struct
{
	queuenode * front; //头指针
	queuenode * rear; //尾指针
}linkqueue;
 
//栈的操作函数
//1.初始化
void initstack(linkstack * l)
{
	*l = (linkstack)malloc(sizeof(stacknode));
	(*l)->next = NULL;
}
//2.进栈操作
void push(linkstack top, char x)
{
	stacknode * temp;
	temp = (stacknode *)malloc(sizeof(stacknode));
	temp->data = x;
	temp->next = top->next;
	top->next = temp;
}
//3.出栈操作
int pop(linkstack top, char * x)
{
	stacknode * temp;
	temp = top->next;
	if (temp == NULL)
	{
		return 0;
	}
	top->next = temp->next;
	*x = temp->data;
	free(temp);
	return  1;
}
 
//队列的操作函数
//1.初始化
void initqueue(linkqueue * q)
{
	q->front = (queuenode *)malloc(sizeof(queuenode));
	q->rear = q->front;
	q->front->next = NULL;
}
//2.入队操作
void enterqueue(linkqueue * q, char y)
{
	queuenode * newnode;
	newnode = (queuenode *)malloc(sizeof(queuenode));
	newnode->data = y;
	newnode->next = NULL;
	q->rear->next = newnode;
	q->rear = newnode;
}
//3.出队操作
int deletequeue(linkqueue * q, char * x)
{
	queuenode * p;
	if (q->front == q->rear)
	{
		return(0);
	}
	p = q->front->next;
	q->front->next = p->next;
	if (p == q->rear)
		q->rear = q->front;
	*x = p->data;
	free(p);
	return(1);
}
 
//主函数
int main(void)
{
	int i = 0, j = 0; //用于循环计数
	int f = 1; //用于控制循环
	char datas = ' ', dataq = ' ';//存放输入数据
	char dataos ;
	char dataoq ; //存放弹出数据
	char data[50];
    linkstack l; //定义栈顶指针
	linkqueue q; //定义队列头指针
	initstack(&l);
	initqueue(&q);
 
	//分别将前半段字符输入栈，后半段输入队列
	printf("请输入需要判断的字符序列");
    scanf("%s",data);
	while (data[i] != '&' && i<=strlen(data)/2)
	{
			push(l, data[i]);
			i++;
	}
    //i为&前面字符的长度
	while (data[i+j+1] != '#' &&i>=j)
	{
			enterqueue(&q, data[i+j+1]);
			j++;
	}
    //j为&到#后面的长度
 
	//将栈和队列中的数据一一弹出比较
	if (i != j)
	{
		printf("此序列不是回文\n");
	}
	else
	{
		for (i = 0; i < j; i++)
		{
			pop(l, &dataos);
			deletequeue(&q, &dataoq);
			if (dataos != dataoq)
			{
				printf("此序列不是回文\n");
				f = 0;
				break;
			}
		}
		if (f)
			printf("此序列是回文\n");
	}
	return 0;
}