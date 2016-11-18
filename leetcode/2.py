# Add Two Numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object): 
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = move = ListNode(0)
        temp = 0
        while l1 and l2:
            move.next = ListNode((l1.val + l2.val + temp) % 10)
            temp = (l1.val + l2.val + temp) / 10
            l1 = l1.next
            l2 = l2.next
            move = move.next
        while l1:
            move.next = ListNode((l1.val + temp) % 10)
            temp = (l1.val + temp) / 10
            l1 = l1.next
            move = move.next
        while l2:
            move.next = ListNode((l2.val + temp) % 10)
            temp = (l2.val + temp) / 10
            l2 = l2.next
            move = move.next
        if temp != 0:
            move.next = ListNode(temp)
        return head.next
