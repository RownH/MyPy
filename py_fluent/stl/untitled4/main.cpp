#include <iostream>
using namespace std;
//大顶堆
template<typename T>
class heap{
    heap(int n):maxN(n){
        m_heap=new T[maxN];
        if(!m_heap){
            throw ("无法申请内存");
        }

    }
    void push(T &newData){
        if(count>maxN){
           return ;
        }
        ++count;
        m_heap[count]=newData;
        int i=count;
        while(i/2>0 && m_heap[i]> m_heap[i/2]){
          swap(m_heap[i],m_heap[i-2]);
          i/=2;
        }
    }
    void pop(){
        if(count<0){
            return ;
        }
        m_heap[0]=m_heap[count];
        heapify(0); //调整堆
    }
    void heapify(int i){
        int maxIdx=i;
        while (i<=count/2) {
            if( m_heap[i]<m_heap[2*i+1]){
                maxIdx=2*i+1;
            }
            if(m_heap[i]<m_heap[2*i+2]){
                maxIdx=2*i+2;
            }
            swap(m_heap[i],m_heap[maxIdx]);
            i=maxIdx;
        }
    }//自顶向下堆化

    void initHeap(){
        for (int i=count/2;i>=1;--i) {
            heapify(i);
        }
    }

private:
  T * m_heap;// 存储数组
  int maxN;
  int count=0;
};


int main()
{
    cout << "Hello World!" << endl;
    return 0;
}
