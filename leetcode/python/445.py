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
        t1 = []
        t2 = []
        while l1:
            t1.append(l1.val)
            l1 = l1.next
        while l2:
            t2.append(l2.val)
            l2 = l2.next
        ret = []
        t = 0
        while t1 and t2:
            a , b = t1.pop(), t2.pop()
            ret.append((a+b+t)%10)
            t = (a + b + t) / 10
        while t1:
            a = t1.pop()
            ret.append((a+t)%10)
            t = (a + t) / 10
        while t2:
            b= t2.pop()
            ret.append((b+t)%10)
            t = (b + t) / 10
        if t != 0:
            ret.append(t)
        h = m = ListNode(0)
        while ret:
            m.next = ListNode(ret.pop())
            m = m.next
        return h.next
