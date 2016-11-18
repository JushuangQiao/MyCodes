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
        ret = []
        temp = 0
        while l1 and l2:
            val = (l1.val + l2.val + temp) % 10
            temp = (l1.val + l2.val + temp) / 10
            ret.append(val)
            print ret
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = (l1.val + temp) % 10
            temp = (l1.val + temp) / 10
            ret.append(val)
            print ret
            l1 = l1.next
        while l2:
            val = (l2.val + temp) % 10
            temp = (l2.val + temp) / 10
            ret.append(val)
            l2 = l2.next
        if temp != 0:
            ret.append(temp)
        return ret
