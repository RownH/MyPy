#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#define MAX_NUMS 100    //定义输入数字最大为100个数
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
int array[MAX_NUMS];
int i=0;
int singnal=0;
void* thread(void *arg)
{
    pthread_detach(pthread_self()); //使线程独自运行
    pthread_mutex_lock(&mutex);
    printf("thread's ID is %d: 请输入任意个数，按回车键结束，统计求和\n",pthread_self());
      do
      {
       scanf("%d",&array[i]);
       i++;
      }while(getchar()!='\n');         //用于判断是否按了回车
     singnal++;         //信号量
    pthread_mutex_unlock(&mutex);
    return NULL;
}

int main()
{
    pthread_t id;
    if (!pthread_create(&
                        id, NULL, thread, NULL)) {
        printf("main thread's ID is %d,anthor thread's ID is %d\n",pthread_self(),id);
    } else {
        printf("Create thread failed!\n");
    }
    while (singnal==0) {}  //循环等待
    pthread_mutex_lock(&mutex); //进入后 加锁 防止出现错误
    int sum=0;
    for(int j=0;j<i;j++)
    {
         sum =sum+array[j];
    }
    printf("thread's ID is %d: 求和 = %d \n",pthread_self(),sum);
    pthread_mutex_unlock(&mutex);

    pthread_mutex_destroy(&mutex);
    return 0;
}

