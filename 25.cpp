class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head) {
            return head;
        }
        ListNode* newHead = new ListNode(0);
        newHead->next = head;
        ListNode* prePtr = newHead;
        ListNode* prePtr2 = newHead;
        ListNode* nextPtr = head;
        ListNode* curPtr = head;
        while (nextPtr) {
            curPtr = group(nextPtr, prePtr,k);
            prePtr2->next = curPtr;
            prePtr2 = prePtr;

        }
        return newHead->next;

    }
    ListNode* group(ListNode *& head, ListNode* &trail, int i) {
        if (!head) {
            return head;
        }
        ListNode* nextPtr = head;
        ListNode* cur = head;
        ListNode* pre = NULL;
        while (nextPtr && i > 0) {
            cur = nextPtr;
            nextPtr = nextPtr->next;
            cur->next = pre;
            pre = cur;
            --i;
        }
        if (i>0) { //当不足以K个时
            nextPtr = cur;
            cur = cur;
            pre = NULL;
            while (nextPtr) {
                cur = nextPtr;
                nextPtr = nextPtr->next;
                cur->next = pre;
                pre = cur;
            }
        }
        trail = head;
        head = nextPtr;
        return cur;
    }
};