/*
面试题06. 从尾到头打印链表
*/
class Solution {
public:
    vector<int> reversePrint(ListNode* head) {
        ListNode *p=revers(head);
        vector<int>res;
        while(p){
            res.push_back(p->val);
            p=p->next;
        }
        return res;
    }
    ListNode* revers(ListNode *head){
        if(head==NULL|| head->next==NULL){
            return head;
        }
        ListNode *res=revers(head->next);
        head->next->next=head;
        head->next=NULL;
        return res;
    }
    ListNode* revers(ListNode *head){
        if(head==NULL|| head->next==NULL){
            return head;
        }
        ListNode *p=head;
        ListNode *q=head->next;
        ListNode *r=head;
        while(q){
            r=q;
            q=q->next;
            r->next=p;
            p=r;
        }
        head->next=NULL;
        return p;
    }
};
