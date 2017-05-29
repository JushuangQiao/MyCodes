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
        pre = pre_m = ListNode(0)
        pre.next = head
        aft = head.next
        flag = 0
        while head and aft:
            if head.val != aft.val:
                if flag:
                    pre_m.next = aft
                    head = aft
                    aft = head.next
                    flag = 0
                else:
                    pre_m = head
                    head = aft
                    aft = head.next
            else:
                aft = aft.next
                head.next = aft
                flag = 1
        if flag:
            pre_m.next = None
        return pre.next
