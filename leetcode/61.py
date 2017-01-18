# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k==0:
            return head
        tail = head
        num = 1
        while tail.next:
            tail = tail.next
            num += 1
        tail.next = head
        k %= num
        while k>0 and num-k:
            head = head.next
            tail = tail.next
            k += 1
        tail.next = None
        return head
        
