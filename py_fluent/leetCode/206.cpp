class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(!head ||!head->next){
            return head;
        }
        ListNode *n=reverseList(head->next);
        head->next->next=head;
        head->next=NULL;
        return n;        
    }
};
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
            if(!head ||!head->next){
                return head;
            }
            ListNode* p=head->next;
            ListNode* q=head;
            ListNode* s=head;
            while(p){
                s=p;
                p=p->next;
                s->next=q;
                q=s;
            }
            head->next=NULL;
            return s;
    }
};