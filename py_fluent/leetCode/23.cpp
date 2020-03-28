class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* p = NULL;
        ListNode* q = NULL;
        ListNode* res = NULL;
        if(lists.size()==0){
            return NULL;
        }
        while (lists.size() > 1) {
            p = lists.back();
            lists.pop_back();
            q = lists.back();
            lists.pop_back();
            res = mergeTwo(p, q);
            lists.push_back(res);
        }
        return lists[0];
    }
    ListNode* mergeTwo(ListNode* one, ListNode* two) {
        ListNode* p = one;
        ListNode* q = two;
        ListNode* res = new ListNode(0);
        ListNode* trial = res;
        ListNode* newNode = NULL;
        while (p && q) {
            if (p->val < q->val) {
                newNode = new ListNode(p->val);
                trial->next = newNode;
                p = p->next;
                trial = trial->next;
            }
            else if (p->val > q->val) {
                newNode = new ListNode(q->val);
                trial->next = newNode;
                q = q->next;
                trial = trial->next;
            }
            else {
                newNode = new ListNode(q->val);
                trial->next = newNode;
                q = q->next;
                trial = trial->next;
                newNode = NULL;
                newNode = new ListNode(p->val);
                trial->next = newNode;
                p = p->next;
                trial = trial->next;
            }
        }
        while (p) {
            newNode = new ListNode(p->val);
            trial->next = newNode;
            trial = trial->next;
            p = p->next;
        }
        while (q) {
            newNode = new ListNode(q->val);
            trial->next = newNode;
            trial = trial->next;
            q = q->next;
        }
        return res->next;
    }
};