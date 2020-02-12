#include <stdio.h>
int main(void)
{
	int a;
	printf("输入你的年龄：");
	scanf_s("%d",&a);
	if(10<=a&&a<=20)
	{
		printf("不愁\n");
	}
	else if(20<a&&a<=30)
	{
		printf("不悔\n");
	}
	else	if(30<a&&a<=40)
	{
		printf("而立\n");
	}
	else	if(40<a&&a<=50)
	{
		printf("不惑\n");
	}
	else		if(50<a&&a<=60)
	{
		printf("知天命\n");
	}
	else	if(60<a&&a<=70)
	{
		printf("耳顺\n");
	}
	else	if(70<a&&a<=80)
	{
		printf("古稀\n");
	}
	else	if(80<a&&a<=90)
	{
		printf("耄耋\n");
	}
	else	if(90<a&&a<=100)
	{
		printf("期颐\n");
	}
				else 
				{
					printf("错误\n");
				}
	
	return 0;
}
