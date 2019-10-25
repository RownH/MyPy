#include <iostream>
#include <fstream>
#include"string.h"

using namespace std;


struct book
{
public:
	char no[20];
	char name[20];
	float price;
};
book a[20];
struct List
{
	book *data;
	int length;
};
	
List list;
int SIZE = 1000;
int init()
{
	list.data = new book[SIZE];
	if (!list.data)
	{
		cout << "分配内存出错！";
		return -1;
	}
	else
		return 0;
}

void input()
{
	int i, j, op, t = 0, n = 0;
	int flog = 0;
	cout << "输入图书信息" << endl;
	for (i = list.length; i < SIZE; i++)
	{
		cout << "书号：";
		cin >> list.data[i].no;
		if (list.length != 0)
		{
			if (flog == 0)
			{
				for (j = 0; j < list.length; j++)
				{
					if (strcmp(list.data[i].no, list.data[j].no) == 0)
					{
						cout << "输入书号存在图书，请重新输入：" << endl;
						cout << "书号" << endl;
						cin >> list.data[i].no;
						flog = 0;
					}
					else
					{
						flog = 1;
						break;
					}
				}
			}
		}
		cout << "书名：";
		cin >> list.data[i].name;
		cout << "价格：";
		cin >> list.data[i].price;
		list.length++;
		cout << "是否继续输入，是（1），否（0）：" << endl;
		cin >> op;
		if (op == 0)
			break;
	}
	system("pause");
}
void ouput()
{
	int i;
	for (i = 0; i <list.length; i++);
	{
		cout << "书号：" << list.data[i].no;
		cout << "\t书名：" << list.data[i].name;
		cout << "\t单价：" << list.data[i].price << endl;
	}
}
int search(book *b, int x)
{
	int i;
	int flag = 0;
	if (x == 1)
	{
		for (i = 0; i < list.length; i++)
		{
			if (strcmp(list.data[i].no, b->no) == 0)
			{
				flag = i + 1;  
				cout << "找到该图书，位置为：" << i + 1 << endl;
				cout << "书号：" << list.data[i].no << "\t书名：" << list.data[i].name << "\t价格：" << list.data[i].price;
				cout << endl;
				break;
			}
		}
		if (flag == 0)
			cout << "没有找到该图书" << endl;
	}
	if (x == 2)
	{
		for (i = 0; i < list.length; i++)
		{
			if (strcmp(list.data[i].name, b->name) == 0)
			{
				flag = i + 1;  
				cout << "找到该图书，位置为：" << i + 1 << endl;
				cout << "书号：" << list.data[i].no << list.data[i].name << list.data[i].price << endl;
				cout << endl;
				break;
			}
		}
		if (flag == 0)
		{
			cout << "没有找到该图书" << endl;

		}
	}
	if (x == 3)
	{
		for (i = 0; i < list.length; i++)
		{
			if (list.data[i].price, b->price)
			{
				flag = i + 1;  
				cout << "找到该图书，位置为：" << i + 1 << endl;
				cout << "书号：" << list.data[i].no << list.data[i].name << list.data[i].price << endl;
				cout << endl;
				break;
			}
		}
	}
	return 0;
	system("pause");
}
void chazhao()
{
	int sel;
	system("cls");  //clears 
	cin >> sel;
	while (sel <= 0 || sel > 5)
	{
		cout << "输入错误，请重新输入" << endl;
		cin >> sel;
	}

	switch (sel)
	{

	case 1:
	{
		book b2;
		cout << "输入图书信息" << endl;
		cout << "书号：";
		cin >> b2.no;
		search(&b2, 1);
		system("pause");
		// menu(); 
		chazhao();
		break;
	}
	case 2:
	{
		book b2;
		cout << "输入图书信息" << endl;
		cout << "书名：";
		cin >> b2.name;
		search(&b2, 2);
		system("pause");
		//menu(); 
		chazhao();
		break;
	}
	case 3:
	{
		book b2;
		cout << "输入图书信息" << endl;
		cout << "价格：";
		cin >> b2.price;
		search(&b2, 3);
		system("pause"); //menu();
		chazhao();
		break;
	}
	case 4:
	{
		int i;
		book b1;
		cout << "输入查找位置" << endl;
		cin >> i;
		i = search(&b1,2);
		cout << "书号：" << b1.no << "\t书名：" << b1.name << "\t价格：" << b1.price << endl;
		system("pause");
		chazhao();
		//menu();
		break;
	}
	}
}
int insert()
{
	book b;
	cout << "输入书号:";
	cin >> b.no;
	cout << "输入书名:";
	cin >> b.name;
	cout << "输入单价:";
	cin >> b.price;

	int i;
	cout << "输入插入的位置：";
	cin >> i;

	if (i<1 || i>list.length + 1)
	{
		cout << "输入错误";
		return 0;
	}

	else
	{
		if (i == list.length + 1)
			list.data[i - 1] = b;
		else
		{
			int k = 0;

			for (k = 0; k < list.length - 1; k++)
			{
				if (k == i - 1)
				{
					for (int j = list.length - 1; j >= k; j--)
						list.data[j + 1] = list.data[j];
				}
			}
			list.data[i - 1] = b;

		}
	}
	list.length++;
	return 1;
}
int del(int x)
{
	int i=1;
	int flag = 0;
	if (x > list.length)
	{
		cout << "输入错误" << endl;
		return 0;
	}
	for (int i = 1; i <= list.length; i++); 
	{
		if (i == x) 
		{
			for (i = i; i <= list.length; i++)
				list.data[i - 1] = list.data[1];
			list.length--;
			flag = 1;
		}
	}
	if (flag = 0) 
	{
		cout << "删除失败" << endl;
	}
	return 0;
}
void change(book *b )
{
	char no[20];
	cout << "输入要修改书号:";
	cin >> no;
	cout << "输入修改完成的书号:";
	cin >> b->no;
	cout << "输入修改完成的书名:";
	cin >> b->name;
	cout << "输入修改完成的单价:";
	cin >> b->price;

	int flag = 0;
	for (int i = 0; i < list.length; i++)
	{
		if (strcmp(list.data[i].no,no) == 0)
		{
			strcpy(list.data[i].no, b->no);
			strcpy(list.data[i].name, b->name);
			list.data[i].price = b->price;
			flag = 1;
			cout << "修改完成！" << endl;
		}
	}
	if (flag == 0)
	{
		cout << "修改失败！" << endl;
	}
}
void sort1() //降序
{
	int i, j, t = 0;
	book m;
	for (j = 0; j <= list.length - 2; j++) 
	{
		for (i = 0; i <= list.length - 2; i++)
		{
			if (list.data[i].price > list.data[i + 1].price)
			{
				//strcpy_s(list.date[i].id, list.date[i + 1].id);
				//strcpy_s(list.date[i].name, list.date[i + 1].name);
				m = list.data[i];
				list.data[i] = list.data[i + 1];
				list.data[i + 1] = m;
			}

		}

	}
	system("pause");
}
void sort2() //升序
{
	int i, j;
	book n;
	for (j = 0; j <= list.length - 2; j++)  
	{
		for (i = 0; i <= list.length - 2; i++)
		{
			if (list.data[i].price < list.data[i + 1].price)
			{
				n = list.data[i];
				list.data[i] = list.data[i + 1];
				list.data[i + 1] = n;
			}

		}
	}
	system("pause");
}

void count()
{
	cout << "共有图书：" << list.length << "本" << endl;
}
int save()
{
	int x;
	cout << "-------------------1.保存------2.退出----------------" << endl;
	cin >> x;
	if (x != 1)
	{
		return 0;
	}
	ofstream outfile("test.txt", ios::out | ios::binary);
	ofstream outfile_list("test_list.txt", ios::out | ios::binary);
	if (!outfile)
	{
		cerr << "打开文件失败！" << endl;
		exit(-1);
	}
	if (!outfile_list)
	{
		cerr << "打开文件失败!" << endl;
		exit(-1);
	}
	for (int i = 0; i < list.length; i++)
	{
		outfile.write((char *)&list.data[i], sizeof(list.data[i]));
	}
	outfile_list.write((char *)&list.length, sizeof(list.length));
	outfile.close();
	outfile_list.close();
	return 0;
}

int read()
{
	cout << "------------------欢迎使用图书读取功能---------------" << endl;
	int x;
	cout << "-------------------1.读取------2.退出----------------" << endl;
	cin >> x;
	if (x != 1)
	{
		return 0;
	}

	ifstream infile("test.txt", ios::binary);
	ifstream infile_list("test_list.txt", ios::binary);
	if (!infile)
	{
		cerr << "打开失败!" << endl;
		exit(0);
	}
	if (!infile_list)
	{
		cerr << "打开失败!" << endl;
		exit(0);
	}

	infile_list.read((char *)&list.length, sizeof(list.length));

	for (int i = 0; i < list.length; i++)
	{
		//infile.seekg(i * sizeof(list.data[i]), ios::beg);
		infile.read((char *)&list.data[i], sizeof(list.data[0]));
	}

	infile.close();
	infile_list.close();
	return 0;
}
void menu()
{
	cout << "------------------欢迎使用图书管理系统---------------" << endl;
	cout << "------------------      0.退出              ---------------" << endl;
	cout << "------------------      1.录入              ---------------" << endl;
	cout << "------------------      2.输出              ---------------" << endl;
	cout << "------------------      3.查找              ---------------" << endl;
	cout << "------------------      4.删除              ---------------" << endl;
	cout << "------------------      5.修改              ---------------" << endl;
	cout << "------------------      6.排序              ---------------" << endl;
	cout << "-----------------       7.计数               ---------------" << endl;
	cout << "-----------------       8.保存               ---------------" << endl;
	cout << "-----------------       9.读取               ---------------" << endl;
}
int main()
{
	book b1 = { "3","3",3 };
	init();
	int n;
	while (1)
	{
		system("pause");
		system("cls");
		menu();
		cout << "输入你的选择：";
		cin >> n;

		if (n == 0)
			break;
		if (n == 1)
			input();
		if (n == 2)
			ouput();
		if (n == 3)
		{
			book b1 = { "3","3",3 };
			search(&b1, 1);
		}
		if (n == 4)
			del(1);
		if (n == 5)
		{
			book b2 = { "7","8",9 };
			change(&b2);
		}
		if (n == 6)
			sort1();
		if (n == 7)
			sort2();
		if (n == 8)
			save();
		if (n == 9)
			read();
	}
}