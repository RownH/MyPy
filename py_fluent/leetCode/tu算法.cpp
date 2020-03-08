/*
	图中得算法，邻接表得深度优先算法与广度优先算法

*/
#include<iostream>
#include<vector>
#include<queue>
using namespace std;
template<typename T>
class LinkedList {
public:
	LinkedList() :node(0) {
		_size = 0;
	}
	LinkedList(T val):node(val) {
		
	}
	void add(int t) {
		LinkedList* newNode = new LinkedList(t);
		newNode->next = this->next;
		this->next = newNode;
		_size++;
	}
	int size() {
		return _size;
	}
	T get(int i) {
		LinkedList* p = this->next;
		for (size_t j = 0; j <i ; j++)
		{
			p = p->next;
		}
		return p->node;
	}
	~LinkedList() {
		if (next) {
			delete next;
		}
	}
private:
	LinkedList* next;
	T node;
	int _size;
};

class Graph {
public:
	Graph(int v) {
		this->v = v;
		list = new LinkedList<int>[v];
	}
	void addEdge(int s, int t) {
		list[s].add(t);
	}
	void bfs(int s, int t) {
		//从s->t
		if (s == t)return;
		queue<int>q;
		bool* visited = new bool[v] ;
		int* prev = new int[v];
		for (int i = 0; i < v; i++) {
			prev[i] = -1;
			visited[i] = 0;
		}
		visited[s] = true;
		q.emplace(s);
		while (!q.empty())
		{
			auto w = q.front();
			q.pop();
			for (int i = 0; i < list[w].size(); i++) {
				int val = list[w].get(i);
				if (!visited[val]) {
					prev[val] = w;
					if (val == t) {
						print(prev,s, t);
					}
					q.push(val);
					visited[val];
				}
			}
		}
	}
	void dfs(int s, int t) {
		bool found = 0;
		bool *visited = new bool[v];
		int* prev = new int[v];
		for (int i = 0; i < v; i++) {
			prev[i] = -1;
			visited[i] = 0;
		}
		recurDfs(s, t,found,visited,prev);
	
	}
	void recurDfs(int w,int t,bool& found,bool* visited,int *prev) {
		if (found == 1) {
			return ;
		}
		visited[w] = 1;
		if (w == t) {
			found = true;
			return;
		}
		for (int i = 0; i < list[w].size(); i++) {
			int q = list[w].get(i);
			if (!visited[q]) {
				prev[q] = w;
				recurDfs(q, t, found, visited, prev);
			}
		}
	}

	void print(int *prev,int s, int t) {
		if (prev[t] != -1 && t != s) {
			print(prev, s, prev[t]);
		}
		cout << t << " ";
	}
	void toboSortByKahn() {
		int* inDegree = new int[v] {0};
		for (int i = 0; i < v; i++) {
			for (int j = 0; j < list[i].size(); j++) {
				auto q=list[i].get(j);
				inDegree[q]++;
			}
		}
		queue<int>que;
		for (int i = 0; i < v; i++) {
			if (inDegree[i] == 0) {
				que.push(i);
			}
		}
		while (!que.empty())
		{
			auto w = que.front();
			cout << w << "->";
			que.pop();
			for (int i = 0; i < list[w].size(); i++) {
				auto q = list[w].get(i);
				inDegree[q]--;
				if (inDegree[q] == 0) {
					que.push(q);
				}
			}

		}
	}
	void toboSortBydfs() {
		bool* visited = new bool[v] {0};
		
		for (int i = 0; i < v; i++) {
			if (!visited[i]) {
				visited[i] = 1;
				topoDfs(i, visited);
			}
		}
	}
	void topoDfs(int w,bool *visited) {
		for (int i = 0; i < list[w].size(); i++) {
			auto q = list[w].get(i);
			if (!visited[q]) {
				visited[q] = 1;
				topoDfs(q, visited);
			}
		}
		cout << w << "->";
	}


private:
	int v;
	LinkedList<int>* list;
};


int main() {
	Graph a(5);
	a.addEdge(0, 1);
	a.addEdge(0, 2);
	a.addEdge(1, 3);
	a.addEdge(1, 4);
	a.addEdge(2, 3);
	a.addEdge(2, 4);
	a.addEdge(3, 4);
	//a.toboSortByKahn();
	a.toboSortBydfs();
}