# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = pre = ListNode(0)
        pre.next = head
        while head and head.next:
            next = head.next
            if head.val == val:
                pre.next, head, next = next, pre.next, head.next
            else:
                pre, head, next = head, next, head.next
        if head and head.val == val:
            pre.next = None
        return p.next

