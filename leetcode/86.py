# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        ret = h = ListNode(0)
        pre = p = ListNode(0)
        while head:
            if head.val < x:
                h.next = head
                h = h.next
            else:
                p.next = head
                p = p.next
            head = head.next
        p.next = None
        h.next = pre.next
        return ret.next