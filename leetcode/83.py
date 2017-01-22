# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        h, m = head, head.next
        while m:
            if h.val == m.val:
                m = m.next
                h.next = m
            else:
                h = h.next
        return head