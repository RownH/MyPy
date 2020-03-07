/*
    2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
*/
#include<iostream>
#include<vector>
using namespace std;
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
    
};
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* p = l1;
        ListNode* q = l2;
        ListNode* pre = p;
        int yu = 0;

        while (p && q) {
            p->val += q->val + yu;
            if (p->val > 9) {
                p->val -= 10;
                yu = 1;
            }
            else {
                yu = 0;
            }
            pre = p;
            p = p->next;
            q = q->next;
        }
        if (p) {
            while (p) {
                p->val = p->val + yu;
                if (p->val > 9) {
                    p->val -= 10;
                    yu = 1;
                }
                else {
                    yu = 0;
                }
                pre = p;
                p = p->next;
            }
        }
        if (q) {
            pre->next = q;
            p = q;
            while (p) {
                p->val = p->val + yu;
                if (p->val > 9) {
                    p->val -= 10;
                    yu = 1;
                }
                else {
                    yu = 0;
                }
                pre = p;
                p = p->next;
            }
        }
        if (yu) {
            ListNode* newNode = new ListNode(1);
            pre->next= newNode;
        }
        return l1;
    }
};

int main() {
    Solution a;
    ListNode* p = new ListNode(1);
    ListNode* q = new ListNode(9);
    q->next = new ListNode(9);
    a.addTwoNumbers(p, q);
}