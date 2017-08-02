# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre_m = pre = ListNode(0)
        pre.next = head
        stack = []
        nums = 1
        while nums < m and head:
            head = head.next
            pre_m = pre_m.next
            pre_m.next = head
            nums += 1
        while m <= nums <= n and head:
            stack.append(head)
            head = head.next
            nums += 1
        while stack:
            pre_m.next = stack.pop()
            pre_m = pre_m.next
        pre_m.next = head
        return pre.next
