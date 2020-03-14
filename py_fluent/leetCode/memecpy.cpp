#include<iostream>
using namespace std;
void MemCopy(char* from, char * to, int n)
{
    if (from == NULL || to == NULL || n < 0)
        return;
    int i;
    if (from <= to)
    {
        for (i = n - 1; i >= 0; i--)
            *((char*)(to + i)) = *((char*)(from + i));
    }
    else
    {
        for (i = 0; i < n; i++)
            *((char*)(to + i)) = *((char*)(from + i));
    }
}
int main() {
    char p[15] = "123456789abc";
    char* q = p + 3;
    MemCopy(q,p, 9);
    cout << p<<endl;
    cout << q<<endl;
}