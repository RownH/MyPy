'''
206. 反转链表
示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """ 方法1
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        if head is None:
            return head;
        self.node1=head;
        if head.next is None:
            return head;
        self.node2=head.next;
        self.node3=head
        while self.node2 is not None:
            self.node3=self.node2.next
            self.node2.next=self.node1;
            if self.node1==head:
                self.node1.next=None;
            self.node1=self.node2;
            self.node2=self.node3
        return self.node1
        ''' 
        if head is None:
            return None
        if head.next is None:
            return head;
        else:
            node=self.reverseList(head.next)
            node.next=head
            if head.next==node:
                head.next=None;
            return node


a=ListNode(1);
b=ListNode(2);
a.next=b;
c=Solution();
d=c.reverseList(a)
while d:
    print(d.val)
    d=d.next
