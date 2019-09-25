'''
请判断一个链表是否为回文链表。
示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true

方法:快慢指针确定中间值
    后面指针逆转
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=head;
        if slow is None:
            return True;
        quick=head.next;
        if quick is None:
            return True;
        while quick is not None and quick.next is not None:
            quick=quick.next.next;
            slow=slow.next;

        pre=None;
        next=None;
        while head!=slow:
            next=head.next;
            head.next=pre;
            pre=head;
            head=next;
        
        print(head.val,pre.val)

        if quick is not None:
            slow=slow.next;
        while pre is not None:
            if pre.val !=slow.val:
                return False;
            else:
                pre=pre.next;
                slow=slow.next;            
        return True;
head=ListNode(1);
secode=ListNode(2);
head.next=secode;
secode.next=None;
c=Solution();
print(c.isPalindrome(head));