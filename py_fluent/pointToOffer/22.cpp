/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* getKthFromEnd(ListNode* head, int k) {
        ListNode *newHead=new ListNode(-1);
        newHead->next=head;
        for(int i=0;i<k-1;i++){
            head=head->next;
            if(head==NULL)return NULL;
        }
        while(head){
            newHead=newHead->next;
            head=head->next;
        }
        return newHead;
    }
};