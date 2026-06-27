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
        if not headA and headB:
            return None
        tailA=headA
        while tailA.next:
            tailA=tailA.next
        tailA.next=headA
        slow=headB
        fast=headA
        intersection_node=None
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                slow=headB
                while slow != fast:
                    slow=slow.next
                    fast=fast.next
                intersection_node=slow
                break
        tailA.next=None
        return intersection_node