# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        pre = ListNode(0)
        h = head
        pre.next, next = head, head.next
        while next:
            head.next, pre, head, next = pre, head, next, next.next
        head.next = pre
        h.next = None
        return head

