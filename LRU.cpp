#include<iostream>
using namespace std;
template<typename T>
struct Node
{
	Node(T val):val(val),next(nullptr) {
		
	}
	
	T val;
	Node* next;
};
template<typename T>
class LRU
{
public:
	LRU() {
		head = new Node<T>(0);
		max = 3;
		curent = 0;
	};
	void insert(int val) {
		
		
		Node<T>* p = head;
		Node<T>* q=NULL;
		Node<T>*trail = NULL;
		while (p->next)
		{
			if (p->next->val == val) {
				q = p->next;
				p->next =p->next->next;
				break;
			}
			trail = p;
			p = p->next;
		}
		if (!q) {
			if (curent >= max) {
				delete p;
				p = NULL;
				trail->next = nullptr;
				
			}
			q = new Node<T>(val);
			++curent;
		}
		q->next = head->next;
		head->next = q;
		
	}
	~LRU() {
		Node<T>* p = head;
		Node<T>* q = head;
		while (p)
		{
			q = p;
			p = p->next;
			delete q;
		}
	};
	void print() {
		Node<T>* p = head;
		while (p)
		{
			cout << p->val;
			p = p->next;
		}
		cout << endl;
	}
private:
	Node<T>*head;
	int max;
	int curent;
};
int main() {
	LRU<int> q;
	q.insert(1);
	q.print();
	q.insert(2);
	q.print();
	q.insert(3);
	q.print();
	q.insert(2);
	q.print();
	q.insert(4);
	q.print();
	q.insert(1);
	q.print();
	q.insert(2);
	q.print();
}