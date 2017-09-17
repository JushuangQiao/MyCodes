# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        m_even = even = head.next
        m_odd = head
        move = even.next
        num = 1
        while move:
            if num % 2 == 0:
                m_even.next = move
                move = move.next
                m_even = m_even.next
            else:
                m_odd.next = move
                move = move.next
                m_odd = m_odd.next
            num += 1
        m_even.next = None
        m_odd.next = even
        return head


