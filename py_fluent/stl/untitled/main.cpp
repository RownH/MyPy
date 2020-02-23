#include <iostream>
#include<array>
using namespace std;
int sqr(int n)
{
    return n*n;
}
int main()
{
    int b;
    cin>>b;
    int a[b];
    const int n=sqr(3);
    //array<int,sqr(3)>x;
    cout<<sizeof (n);

    return 0;
}
