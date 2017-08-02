# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        end = ListNode(0)
        while head:
            if head.next == end:
                return True
            tmp = head.next
            head.next = end
            head = tmp
        return False
