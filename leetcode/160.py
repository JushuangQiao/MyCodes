# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lena = lenb = 0
        ma, mb = headA, headB
        while ma:
            lena += 1
            ma = ma.next
        while mb:
            lenb += 1
            mb = mb.next
        ma, mb = headA, headB
        while lena > lenb:
            ma = ma.next
            lena -= 1
        while lenb > lena:
            mb = mb.next
            lenb -= 1
        while lena:
            if ma == mb:
                return ma
            else:
                ma = ma.next
                mb = mb.next
            lena -= 1
        return None