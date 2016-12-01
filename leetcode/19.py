# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Node is null
        if not head:
            return None
        # Node is less than n
        if head.next == None and n > 1:
            return None
        q = head
        for i in range(n):
            if q == None:
                return None
            q = q.next
        # Nodes is equal to n
        if q == None:
            return head.next
        # Nodes is more than n
        ret = p = ListNode(0)
        p.next = head
        while q != None:
            q = q.next
            p = p.next
        p.next = p.next.next
        return ret.next
